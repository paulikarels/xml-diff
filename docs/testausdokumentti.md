# Testausdokumentti

### Miten testataan

Projektin testaus perustuu päänsääntöisesti toiminnallisuuteen katettaviin yksikkötesteihin. Suorituskykytestejä en ole vielä tehnyt, mutta nekin tulevat tehtyä myöhemmin. Myös aion lisätä lisää perustoiminnallisuustestejä ja ehkä integraatiotestejä käyttöliittymän testaamiseksi.


### Yksikkötestit

Valtaosa projektin testeistä on yksikkötesteja, joiden pohja kohdistuu kaiikke luokille ja metodeille, poislukien pieniä poikkeuksia.

### Integraatiotestit

TODO: ?

### Suorituskykytestit

TODO:

### Testisyötteet

LZW- ja Huffman-algoritmit voivat toimia eri tavoin riippuen syötteiden koosta ja sisällöstä, testisyötteet koostuvat erikokoisista ja -sisältöisistä .txt-tiedostoista. 
Tällä hetkellä tekstisyötteet kattavat seuraavat:
- **Tyhjät syötteet**, eivät siis sisällä mitään.
- **Lyhyet tekstit**, sisältävät yksinkertaisia ja toistuvia merkkejä.
- **Pitkät tekstit**, laajempi sanakirja ja enemmän erikoismerkkejä tai muita harvinaisempia merkkejä.
- **Erilaiset merkistöt**, kuten aakkoset, numerot ja erikoismerkit, jne.


TODO, Tulevaisuutta liittyen:
Testien tavoitteena on tutkia algoritmien suorituskykyä ja tarkkuutta eri kokoisilla tiedostoilla, jotka sisältävät vaihtelevaa merkistöä.

### Testien suorittaminen

Testit saa ajettua  projektin juurikansiossa komennolla:

```
poetry run pytest
```

### Testien kattavuuden mittaaminen

Testien kattavuuden saa selville projektin juurikansiossta ajamalla komennon:

```
poetry run  coverage run -m pytest
```

Kattavuusraportin taas saa ajettua komennolla:

```
poetry run coverage report --omit="tests/*"
```

Yksikkötestien kattavuus on hyvällä mallilla huffmanin- ja LZW:n -puolella.

```
Name                                        Stmts   Miss  Cover
---------------------------------------------------------------
compression_comparison\__init__.py              0      0   100%
compression_comparison\huffman\huffman.py      94     10    89%
compression_comparison\lzw\bitio.py            70     11    84%
compression_comparison\lzw\lzw.py              73      4    95%
---------------------------------------------------------------
TOTAL                                         237     25    89%
```