"""Create a weekly log for the French L2 maths prep.

Usage:
    python prepa_week.py 1 "Modes de raisonnement" --chap "Modes de raisonnement"
    python prepa_week.py 2 "Fonctions et continuité" --chap "2"

Creates prepa-L2/Semaine_01_Modes_de_raisonnement/ with a README.md template
and an images/ folder for photos of handwritten exercises.
"""
import argparse
import datetime
import os
import re

TEMPLATE = """# Semaine {week:02d} — {topic}

**Dates :** {start} → {end}
**Source :** Pearson *Mathématiques L1* (Marco & Lazzarini), chapitre {chap}
**Temps total :** … h

---

## 1. Ce que j'ai étudié
> Définitions, théorèmes et méthodes clés de la semaine, avec mes propres mots.

- **Définition — …** :
- **Théorème — …** :
- **Méthode — …** :

## 2. Exercices résolus à la main
> 2 ou 3 exercices, rédigés comme à l'examen. Photo du brouillon dans `images/`.

### Exercice 1 (p. …)
**Énoncé :**

**Solution :**

<!-- ![Exercice 1](images/ex1.jpg) -->

### Exercice 2 (p. …)
**Énoncé :**

**Solution :**

## 3. Vérification NumPy (optionnel)
> Seulement si le sujet s'y prête (matrices, déterminants, DL…).

```python
import numpy as np
```

## 4. Difficultés / à revoir
-

## 5. Vocabulaire FR ↔ EN
| Français | English |
|---|---|
|  |  |
"""


def slug(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "_", text.strip())


def main():
    parser = argparse.ArgumentParser(description="Create a weekly prepa-L2 log.")
    parser.add_argument("week", type=int, help="Week number, e.g. 1")
    parser.add_argument("topic", type=str, help='Topic in quotes, e.g. "Modes de raisonnement"')
    parser.add_argument("--chap", type=str, default="…", help="Pearson chapter number(s)")
    args = parser.parse_args()

    folder = os.path.join("prepa-L2", f"Semaine_{args.week:02d}_{slug(args.topic)}")
    path = os.path.join(folder, "README.md")
    if os.path.exists(path):
        print(f"⚠️  {path} already exists, nothing changed.")
        return

    os.makedirs(os.path.join(folder, "images"), exist_ok=True)
    open(os.path.join(folder, "images", ".gitkeep"), "w").close()

    today = datetime.date.today()
    end = today + datetime.timedelta(days=6)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(week=args.week, topic=args.topic, chap=args.chap,
                                start=today.isoformat(), end=end.isoformat()))
    print(f"✅ Created {path}")


if __name__ == "__main__":
    main()
