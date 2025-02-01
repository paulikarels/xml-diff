# Testausdokumentti

### Miten testataan

Projektin testaus perustuu päänsääntöisesti toiminnallisuuteen katettaviin yksikkötesteihin. Suorituskykytestejä en ole vielä tehnyt, mutta nekin tulevat tehtyä myöhemmin. Myös aion lisätä lisää perustoiminnallisuustestejä ja ehkä integraatiotestejä käyttöliittymän testaamiseksi.


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

Yksikkötestien kattavuus on ihan ok, ainakin huffmanin puolella. LZW algoritim testit ovat vasta alkuvaiheessa, mutta ydinrakenne tulisi olla toiminassa.

```
Name                                        Stmts   Miss  Cover
---------------------------------------------------------------
compression_comparison\__init__.py              0      0   100%
compression_comparison\huffman\huffman.py      94     10    89%
compression_comparison\lzw\bitio.py            54      4    93%
compression_comparison\lzw\lzw.py              89     41    54%
---------------------------------------------------------------
TOTAL                                         237     55    77%
```