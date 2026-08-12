#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Régénère llms-full.txt à partir des pages HTML publiées.

llms.txt est la fiche courte, écrite à la main. llms-full.txt est sa version longue :
le texte réel de chaque page, sans navigation ni pied de page, pour les assistants qui
veulent la matière complète sans charger quinze pages de HTML.

Usage, depuis la racine du dépôt :  python3 .claude/build-llms-full.py
À relancer après toute modification de contenu, sinon le fichier ment.
Ajouter une page au site = ajouter une ligne à PAGES ci-dessous.

Ce générateur est le seul du dépôt : il est arrivé avec le lot du 11 août 2026 et a
remplacé une première version qui ne connaissait pas les deux articles.
"""
import re, sys, os
from datetime import date

BASE = "https://une2cvmillehistoires.re"

PAGES = [
    ("index.html", "Accueil", "/"),
    ("mariage.html", "Voiture de mariage", "/mariage"),
    ("demande-en-mariage-2cv.html", "Demande en mariage en 2CV", "/demande-en-mariage-2cv"),
    ("tarifs.html", "Tarifs", "/tarifs"),
    ("location-2cv-reunion.html", "Location de 2CV à La Réunion", "/location-2cv-reunion"),
    ("evjf-evjg.html", "EVJF et EVJG", "/evjf-evjg"),
    ("evjf-evjg-chasse-au-tresor.html", "EVJF & EVJG : chasse au trésor et jeux lontan", "/evjf-evjg-chasse-au-tresor"),
    ("balades.html", "Balades", "/balades"),
    ("shooting-evenements.html", "Shootings et évènements", "/shooting-evenements"),
    ("rosalie-et-soizig.html", "Rosalie et Soizig, les deux voitures", "/rosalie-et-soizig"),
    ("histoires.html", "Histoires de mariages — le carnet", "/histoires"),
    ("histoires/emma-fabien.html", "Récit : Emma & Fabien, un mariage en 2CV dans l'Ouest",
     "/histoires/emma-fabien"),
    ("faq.html", "Questions fréquentes", "/faq"),
    ("contact.html", "Contact", "/contact"),
    ("mentions-legales.html", "Mentions légales", "/mentions-legales"),
]

BLOCS = ("p|div|section|h1|h2|h3|h4|h5|h6|li|tr|br|header|footer|nav|article|"
         "figcaption|blockquote|details|summary|dd|dt|option|label|main|form")

ENT = {"&nbsp;": " ", "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"',
       "&#39;": "'", "&eacute;": "é", "&agrave;": "à", "&laquo;": "«",
       "&raquo;": "»", "&hellip;": "…", "&mdash;": "—", "&ndash;": "–",
       "&times;": "×", "&frac12;": "½", "&deg;": "°", "&euro;": "€",
       "&rsquo;": "'", "&oelig;": "œ", "&ccedil;": "ç", "&egrave;": "è"}


def texte(html):
    s = html
    # on ne garde que le corps
    m = re.search(r"<body[^>]*>(.*)</body>", s, re.S | re.I)
    if m:
        s = m.group(1)
    # éléments non textuels
    s = re.sub(r"<(script|style|svg|template|noscript)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    # menu de navigation et pied de page (répétés sur chaque page)
    s = re.sub(r"<nav\b.*?</nav>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<footer\b.*?</footer>", " ", s, flags=re.S | re.I)
    s = re.sub(r'<a class="skip".*?</a>', " ", s, flags=re.S | re.I)
    s = re.sub(r'<a[^>]*class="[^"]*wa-float[^"]*".*?</a>', " ", s, flags=re.S | re.I)
    # sauts de ligne aux frontières de blocs
    s = re.sub(r"</?(%s)\b[^>]*>" % BLOCS, "\n", s, flags=re.I)
    # toutes les autres balises deviennent des espaces (inline)
    s = re.sub(r"<[^>]+>", " ", s)
    for a, b in ENT.items():
        s = s.replace(a, b)
    s = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), s)
    # nettoyage
    lignes = []
    for l in s.split("\n"):
        l = re.sub(r"[ \t\r ]+", " ", l).strip()
        if l:
            lignes.append(l)
    # dédoublonnage des lignes consécutives identiques
    out = []
    for l in lignes:
        if not out or out[-1] != l:
            out.append(l)
    return "\n".join(out)


def main(rep, date_fr):
    parts = ["# Une 2CV, mille histoires — texte intégral du site", "",
             "> Location de Citroën 2CV de collection AVEC chauffeur à La Réunion (974) :",
             "> voiture de mariage, EVJF/EVJG, balades, shootings et évènements.",
             "> Aucune location sans chauffeur.",
             "> Fiche courte : %s/llms.txt" % BASE,
             "> Généré le %s à partir des pages publiées." % date_fr, "", ""]
    for f, titre, url in PAGES:
        p = os.path.join(rep, f)
        if not os.path.exists(p):
            print("  ! page absente :", f); continue
        t = texte(open(p, encoding="utf-8").read())
        parts.append("---")
        parts.append("")
        parts.append("## " + titre)
        parts.append("Source : %s%s" % (BASE, url))
        parts.append("")
        parts.append(t)
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


if __name__ == "__main__":
    MOIS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet",
            "août", "septembre", "octobre", "novembre", "décembre")
    aujourdhui = date.today()
    defaut = "%d %s %d" % (aujourdhui.day, MOIS[aujourdhui.month - 1], aujourdhui.year)
    # Par défaut : la racine du dépôt, c'est-à-dire le dossier qui contient .claude/
    rep = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    date_fr = sys.argv[2] if len(sys.argv) > 2 else defaut
    open(os.path.join(rep, "llms-full.txt"), "w", encoding="utf-8").write(main(rep, date_fr))
    print("llms-full.txt régénéré :", os.path.getsize(os.path.join(rep, "llms-full.txt")), "octets")
