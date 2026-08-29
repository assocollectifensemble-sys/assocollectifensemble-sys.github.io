# -*- coding: utf-8 -*-
"""
Refonte du gras d'artisans.html selon une regle unique.

REGLE : le gras porte le fait qui aide a CHOISIR entre deux artisans du meme
metier. Rien d'autre.

En pratique :
  - le nom n'est JAMAIS en gras : il est deja un lien, donc deja saillant.
    Le mettre en gras double le signal et noie le reste.
  - le lieu n'est en gras QUE si on s'y rend (boutique, salon d'essayage,
    lieu de reception). Un photographe se deplace sur toute l'ile : ou se
    trouve son studio n'aide personne a le choisir.
  - l'emotion n'est jamais en gras.
  - un seul gras par fiche quand un seul fait departage.
"""
import io, re

CHEMIN = 'artisans.html'

# (ancien, nouveau) - applique dans l'ordre, chacun doit matcher exactement 1 fois
REMPLACEMENTS = [
    # ---------- chapeau : on ne garde que la promesse concrete ----------
    ('Je ne mets ici que <strong>des artisans que j\'ai vus travailler</strong>, de mes yeux',
     'Je ne mets ici que des artisans que j\'ai vus travailler, de mes yeux'),
    ('cette page peut <strong>vous faire gagner du temps</strong>',
     'cette page peut <strong>vous faire gagner du temps</strong>'),  # garde : c'est le benefice

    # ---------- fleuriste : la boutique se visite, le lieu compte ----------
    ('<strong>Happiness Blossom</strong></a><br>Pauline, <strong>\u00e0 Saint-Leu et Trois-Bassins</strong>.',
     'Happiness Blossom</a><br>Pauline, <strong>boutique \u00e0 Saint-Leu et Trois-Bassins</strong>.'),

    # ---------- photographes : le lieu ne departage rien, le service oui ----------
    ('<strong>Alexandre Bertucat Photography</strong></a><br>Studio <strong>au Tampon</strong>. '
     'Mariages, portraits, grossesse, naissance.',
     'Alexandre Bertucat Photography</a><br>Mariages, portraits, <strong>grossesse et naissance</strong> '
     '\u2014 il suit les familles au-del\u00e0 du jour J.'),

    ('<strong>Matmatoff</strong></a><br>Photographe <strong>et vid\u00e9aste</strong> \u2014 c\'est la diff\u00e9rence : '
     'la photo et le film de la journ\u00e9e par la m\u00eame personne.',
     'Matmatoff</a><br><strong>Photographe et vid\u00e9aste</strong> : la photo et le film de la journ\u00e9e '
     'par la m\u00eame personne, un seul interlocuteur.'),

    ('<strong>Erwan L\'Haridon</strong></a><br>Mariages, couples et familles.',
     'Erwan L\'Haridon</a><br>Mariages, couples et familles.'),

    ('<strong>Carmen Legros</strong></a><br>\u00ab\u00a0Du vrai, de l\'\u00e9motion, et du fun\u00a0\u00bb. '
     'Mariage, couple, famille, et aussi les artisans au travail. Elle se d\u00e9place <strong>jusqu\'\u00e0 Maurice</strong>.',
     'Carmen Legros</a><br>\u00ab\u00a0Du vrai, de l\'\u00e9motion, et du fun\u00a0\u00bb. Mariage, couple, famille, '
     'et aussi les artisans au travail. Elle se d\u00e9place <strong>jusqu\'\u00e0 Maurice</strong>.'),

    # ---------- robes : on se deplace en boutique, le lieu compte vraiment ----------
    ('<strong>La Mari\u00e9e Chic</strong></a><br>\u00c0 <strong>Saint-Pierre</strong>, robes de mari\u00e9e et '
     'costumes cr\u00e9\u00e9s sur mesure, sur rendez-vous.',
     'La Mari\u00e9e Chic</a><br>\u00c0 Saint-Pierre, robes de mari\u00e9e et costumes <strong>cr\u00e9\u00e9s sur mesure</strong>, '
     'sur rendez-vous.'),

    ('<strong>Les Secrets d\'Agap\u00e9</strong></a><br>Murielle Hoarau, <strong>au Tampon</strong>. '
     'Salons priv\u00e9s, temps long, robes choisies avec exigence. Elle peut venir habiller la mari\u00e9e chez elle le jour J.',
     'Les Secrets d\'Agap\u00e9</a><br>Murielle Hoarau, au Tampon. Salons priv\u00e9s, temps long, robes choisies '
     'avec exigence. Elle peut <strong>venir habiller la mari\u00e9e chez elle le jour J</strong>.'),

    # ---------- lieu de reception : ici le lieu EST le produit ----------
    ('<strong>Villa Leu Marais Salant</strong></a><br>\u00c0 <strong>Saint-Leu</strong>, face au lagon. '
     'C\'est l\u00e0 qu\'on a fait un <strong>shooting d\'inspiration</strong> \u00e0 plusieurs prestataires du mariage, '
     'la 2CV gar\u00e9e dans le jardin. Un lieu qu\'on peut privatiser pour une r\u00e9ception.',
     'Villa Leu Marais Salant</a><br>\u00c0 <strong>Saint-Leu, face au lagon</strong>. C\'est l\u00e0 qu\'on a fait un '
     'shooting d\'inspiration \u00e0 plusieurs prestataires du mariage, la 2CV gar\u00e9e dans le jardin. '
     'Un lieu <strong>qu\'on peut privatiser</strong> pour une r\u00e9ception.'),

    # ---------- traiteur : ce qui departage = il a son propre lieu ----------
    ('<strong>Chef Romain Durand</strong></a><br>Traiteur et organisation compl\u00e8te. '
     'Il travaille <strong>avec les agriculteurs locaux</strong> et re\u00e7oit aussi dans son propre lieu, '
     '<strong>Le Vieux Pressoir</strong>.',
     'Chef Romain Durand</a><br>Traiteur et organisation compl\u00e8te, avec les agriculteurs locaux. '
     'Il re\u00e7oit aussi <strong>dans son propre lieu, Le Vieux Pressoir</strong> \u2014 traiteur et salle au m\u00eame endroit.'),

    # ---------- patisserie ----------
    ('<strong>Tikatoune</strong></a><br>Delphine, p\u00e2tisserie fine et service traiteur.',
     'Tikatoune</a><br>Delphine, <strong>p\u00e2tisserie fine et service traiteur</strong>.'),
]


def main():
    s = io.open(CHEMIN, encoding='utf-8').read()
    avant_txt = re.sub(r'<[^>]+>', '', s)
    avant_gras = s.count('<strong>')

    for vieux, neuf in REMPLACEMENTS:
        n = s.count(vieux)
        if n != 1:
            raise SystemExit('MATCH %d (attendu 1) pour : %s' % (n, vieux[:70]))
        s = s.replace(vieux, neuf, 1)

    io.open(CHEMIN, 'w', encoding='utf-8').write(s)

    # controles
    d = 0
    for t in re.findall(r'</?strong>', s):
        d += 1 if t == '<strong>' else -1
        assert 0 <= d <= 1, 'strong imbrique'
    assert d == 0, 'strong non ferme'

    for para in re.findall(r'<p[^>]*>(.*?)</p>', s, re.S):
        n = para.count('<strong>')
        if n > 2:
            print('  ATTENTION %d gras :' % n, re.sub(r'<[^>]+>', '', para)[:60])

    print('gras : %d -> %d' % (avant_gras, s.count('<strong>')))
    print('gras restants :')
    for g in re.findall(r'<strong>([^<]+)</strong>', s):
        print('   -', g)


if __name__ == '__main__':
    main()
