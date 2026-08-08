#!/usr/bin/env python3
"""Régénère llms-full.txt à partir du texte visible des pages.

llms.txt tient la fiche courte, écrite à la main : c'est elle qu'on relit et qu'on
corrige. llms-full.txt est sa version longue — le texte réel de chaque page, sans
navigation ni pied de page — pour les assistants qui veulent la matière complète
sans avoir à charger onze pages de HTML.

Usage, depuis la racine du dépôt :  python3 .claude/build-llms-full.py
À relancer après toute modification de contenu.
"""

import html
import re
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SITE = "https://une2cvmillehistoires.re"

# Ordre volontaire : on commence par ce qu'on veut voir cité en premier.
PAGES = [
    ("index.html", "/", "Accueil"),
    ("mariage.html", "/mariage", "Voiture de mariage"),
    ("tarifs.html", "/tarifs", "Tarifs"),
    ("location-2cv-reunion.html", "/location-2cv-reunion", "Location de 2CV à La Réunion"),
    ("evjf-evjg.html", "/evjf-evjg", "EVJF et EVJG"),
    ("balades.html", "/balades", "Balades"),
    ("shooting-evenements.html", "/shooting-evenements", "Shootings et évènements"),
    ("rosalie-et-soizig.html", "/rosalie-et-soizig", "Rosalie et Soizig, les deux voitures"),
    ("histoires.html", "/histoires", "Histoires de mariages"),
    ("faq.html", "/faq", "Questions fréquentes"),
    ("contact.html", "/contact", "Contact"),
    ("mentions-legales.html", "/mentions-legales", "Mentions légales"),
]

MOIS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre")


def texte_visible(source: str) -> str:
    """Le contenu que lit un visiteur : ni <head>, ni menu, ni pied de page, ni icônes."""
    for bloc in ("script", "style", "nav", "svg", "audio", "head", "footer", "noscript"):
        source = re.sub(rf"(?is)<{bloc}\b.*?</{bloc}>", " ", source)
    source = re.sub(r"(?is)<button\b.*?</button>", " ", source)
    # Une frontière d'espace autour de chaque balise évite de coller deux mots.
    source = re.sub(r"<[^>]+>", " ", source)
    source = html.unescape(source)
    source = re.sub(r"[^\S\n]+", " ", source)
    source = re.sub(r" ?\n ?", "\n", source)
    source = re.sub(r"\n{2,}", "\n", source)
    lignes = [ligne.strip() for ligne in source.split("\n")]
    lignes = [ligne for ligne in lignes if ligne and ligne != "Aller au contenu"]
    return "\n".join(lignes)


def main() -> None:
    aujourdhui = date.today()
    morceaux = [
        "# Une 2CV, mille histoires — texte intégral du site",
        "",
        "> Location de Citroën 2CV de collection AVEC chauffeur à La Réunion (974) :",
        "> voiture de mariage, EVJF/EVJG, balades, shootings et évènements.",
        "> Aucune location sans chauffeur.",
        f"> Fiche courte : {SITE}/llms.txt",
        f"> Généré le {aujourdhui.day} {MOIS[aujourdhui.month - 1]} {aujourdhui.year}"
        " à partir des pages publiées.",
        "",
    ]

    for fichier, url, titre in PAGES:
        chemin = RACINE / fichier
        if not chemin.exists():
            raise SystemExit(f"Page absente : {fichier}")
        morceaux += [
            "",
            "---",
            "",
            f"## {titre}",
            f"Source : {SITE}{url}",
            "",
            texte_visible(chemin.read_text(encoding="utf-8")),
        ]

    sortie = RACINE / "llms-full.txt"
    sortie.write_text("\n".join(morceaux).rstrip() + "\n", encoding="utf-8")
    print(f"{sortie.relative_to(RACINE)} — {sortie.stat().st_size // 1024} Ko")


if __name__ == "__main__":
    main()
