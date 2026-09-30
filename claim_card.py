#!/usr/bin/env python3
"""Make a source-linked claim card from a published JevBench result JSON."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

WORDS = {
    "en": {"title": "Decision model evidence card", "model": "Model", "metric": "Hard-tier accuracy", "sample": "Items", "coverage": "Coverage", "license": "License", "source": "Result source", "hash": "Input SHA-256", "limit": "Limit", "caveat": "This card reformats a reported aggregate. It does not rerun the benchmark; uncertainty cannot be estimated reliably from this file alone."},
    "fr": {"title": "Fiche de preuve d'un modèle de décision", "model": "Modèle", "metric": "Exactitude du niveau difficile", "sample": "Exemples", "coverage": "Couverture", "license": "Licence", "source": "Source du résultat", "hash": "SHA-256 du fichier", "limit": "Limite", "caveat": "Cette fiche reformate un résultat agrégé publié. Elle ne relance pas le benchmark ; ce fichier seul ne permet pas d'estimer correctement l'incertitude."},
    "es": {"title": "Ficha de evidencia de un modelo de decisión", "model": "Modelo", "metric": "Exactitud del nivel difícil", "sample": "Ejemplos", "coverage": "Cobertura", "license": "Licencia", "source": "Fuente del resultado", "hash": "SHA-256 del archivo", "limit": "Límite", "caveat": "Esta ficha reformatea un resultado agregado publicado. No vuelve a ejecutar la prueba; este archivo por sí solo no permite estimar bien la incertidumbre."},
}


def card(data, source_url, digest, lang="en"):
    if not isinstance(data, dict) or not isinstance(data.get("hard"), dict):
        raise ValueError("expected JevBench addition JSON with a hard result")
    hard = data["hard"]
    accuracy = hard.get("accuracy")
    count = hard.get("n_items")
    coverage = hard.get("coverage")
    if isinstance(accuracy, bool) or not isinstance(accuracy, (float, int)) or not 0 <= accuracy <= 1:
        raise ValueError("hard.accuracy must be between 0 and 1")
    if type(count) is not int or count < 1:
        raise ValueError("hard.n_items must be a positive integer")
    if not isinstance(source_url, str) or not re.fullmatch(r"https://[^\s()<>]+", source_url):
        raise ValueError("a public HTTPS source URL is required")
    w = WORDS[lang]
    def escape(value):
        return re.sub(r"([\\`*_{}\[\]<>])", r"\\\1", str(value).replace("\n", " "))
    name = escape(data.get("display") or data.get("key") or "unknown")
    license_name = escape(data.get("licence") or "unspecified")
    lines = [f"# {w['title']}: {name}", "", f"- **{w['model']}:** {name}",
             f"- **{w['metric']}:** {accuracy:.1%}", f"- **{w['sample']}:** {count}"]
    if isinstance(coverage, (float, int)) and not isinstance(coverage, bool):
        lines.append(f"- **{w['coverage']}:** {coverage:.1%}")
    lines += [f"- **{w['license']}:** {license_name}",
              f"- **{w['source']}:** [{source_url}]({source_url})",
              f"- **{w['hash']}:** `{digest}`", "", f"**{w['limit']}:** {w['caveat']}"]
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("demo", "render"))
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--source-url")
    parser.add_argument("--lang", choices=WORDS, default="en")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    path = Path(__file__).parent / "fixtures" / "synthetic-jevbench.json" if args.command == "demo" else args.path
    if not path:
        parser.error("render requires a JevBench result JSON path")
    source = "https://example.org/synthetic-result" if args.command == "demo" else args.source_url
    try:
        raw = path.read_bytes()
        output = card(json.loads(raw), source, hashlib.sha256(raw).hexdigest(), args.lang)
        if args.out:
            args.out.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
