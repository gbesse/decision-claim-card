# Decision Claim Card

**Put the source, sample size and limits beside a decision-model benchmark claim.**

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md)

## Related projects

- [JevBench](https://github.com/fstandhartinger/jevbench) — Publishes the real JSON format this tool reads.
- [Kev](https://github.com/jaredpalmer/kev) — Provides another decision-model benchmark and comparison workflow.
- [Jeeves](https://github.com/PostHog/jeeves) — Publishes performance claims that would benefit from a reproducible source card.

Links describe technical neighbors, not an affiliation.

## Try it

```sh
python3 claim_card.py demo --lang en
```

## What this checks

Reads JevBench addition JSON, extracts hard-tier accuracy and sample size, hashes the input and renders a small Markdown evidence card in English, French or Spanish.

## Use with your data

```sh
curl -fsSL https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.2/additions/jeff.json -o /tmp/jevbench-jeff.json
python3 claim_card.py render /tmp/jevbench-jeff.json --source-url https://github.com/fstandhartinger/jevbench/blob/main/results/v1.2/additions/jeff.json --lang en
```

Download a published JevBench addition result and run `render` with its public source URL. A real Jeff result file was parsed during launch.

## Scope and limits

The card reformats someone else’s aggregate; it does not rerun the model or establish an independent ranking. No confidence interval is computed from incomplete aggregate data. The fixture is explicitly synthetic.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

MIT · v0.1.0-alpha.1
