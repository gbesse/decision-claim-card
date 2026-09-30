# Decision Claim Card

**Placez source, taille de l’échantillon et limites à côté d’un chiffre de benchmark.**

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md)

## Projets voisins

- [JevBench](https://github.com/fstandhartinger/jevbench) — Publie le vrai format JSON lu par cet outil.
- [Kev](https://github.com/jaredpalmer/kev) — Fournit un autre benchmark et un workflow de comparaison.
- [Jeeves](https://github.com/PostHog/jeeves) — Publie des chiffres qui gagneraient à avoir une fiche de source reproductible.

Ces liens décrivent des projets voisins, sans affiliation.

## Essayer

```sh
python3 claim_card.py demo --lang fr
```

## Ce que cet outil vérifie

Lit un JSON d’ajout JevBench, extrait exactitude et taille du niveau difficile, hache le fichier et produit une fiche Markdown en français, anglais ou espagnol.

## Utiliser avec vos données

```sh
curl -fsSL https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.2/additions/jeff.json -o /tmp/jevbench-jeff.json
python3 claim_card.py render /tmp/jevbench-jeff.json --source-url https://github.com/fstandhartinger/jevbench/blob/main/results/v1.2/additions/jeff.json --lang fr
```

Téléchargez un résultat JevBench publié et lancez `render` avec son URL publique. Un vrai fichier de résultat Jeff a été lu lors du lancement.

## Périmètre et limites

La fiche reformate un agrégat d’autrui ; elle ne relance pas le modèle et ne prouve aucun classement indépendant. Aucun intervalle n’est calculé à partir de données insuffisantes. La fixture est explicitement synthétique.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

MIT · v0.1.0-alpha.1
