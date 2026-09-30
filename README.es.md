# Decision Claim Card

**Coloque fuente, tamaño de muestra y límites junto a una cifra de benchmark.**

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md)

## Proyectos relacionados

- [JevBench](https://github.com/fstandhartinger/jevbench) — Publica el formato JSON real leído por esta herramienta.
- [Kev](https://github.com/jaredpalmer/kev) — Ofrece otro benchmark y flujo de comparación.
- [Jeeves](https://github.com/PostHog/jeeves) — Publica cifras que ganarían con una ficha de origen reproducible.

Estos enlaces describen proyectos relacionados, sin afiliación.

## Probar

```sh
python3 claim_card.py demo --lang es
```

## Qué comprueba esta herramienta

Lee un JSON de JevBench, extrae exactitud y tamaño del nivel difícil, calcula el hash y produce una ficha Markdown en español, inglés o francés.

## Usar con sus datos

```sh
curl -fsSL https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.2/additions/jeff.json -o /tmp/jevbench-jeff.json
python3 claim_card.py render /tmp/jevbench-jeff.json --source-url https://github.com/fstandhartinger/jevbench/blob/main/results/v1.2/additions/jeff.json --lang es
```

Descargue un resultado JevBench publicado y ejecute `render` con su URL pública. Se leyó un archivo real de Jeff durante el lanzamiento.

## Alcance y límites

La ficha reformatea un agregado de terceros; no ejecuta el modelo ni prueba un ranking independiente. No calcula intervalos con datos insuficientes. El ejemplo es explícitamente sintético.

## Pruebas

```sh
python3 -m unittest discover -s tests -v
```

MIT · v0.1.0-alpha.1
