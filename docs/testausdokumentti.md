# Testausdokumentti

### Miten testataan

Projektin testaus perustuu päänsääntöisesti toiminnallisuuteen katettaviin yksikkötesteihin. Suorituskykytestejä en ole vielä tehnyt, mutta nekin tulevat tehtyä myöhemmin. Myös aion lisätä lisää perustoiminnallisuustestejä ja ehkä integraatiotestejä käyttöliittymän testaamiseksi.


### Yksikkötestit

Valtaosa projektin testeistä on yksikkötesteja, joiden pohja kohdistuu kaiikke luokille ja metodeille, poislukien pieniä poikkeuksia.

### Integraatiotestit

TODO: ?

### Suorituskykytestit
Suorituskykytestien ajamiseen menee tällä hetkellä noin minuutti (suurin tiedosto 10MB), joista saadan vastaa raportti:

Väliaikainen tilanne Huffmanin-koodauksen suorituskykytestien tuloksista. 
```
tests\huffman_performance_test.py ......                                                                                                                                                                          [100%]

-------------------------------------------------------------------------------------------------- benchmark: 6 tests -------------------------------------------------------------------------------------------------  
Name (time in ms)                              Min                   Max                  Mean              StdDev                Median                 IQR            Outliers      OPS            Rounds  Iterations  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
test_compression_performance_1MB           68.9780 (1.0)         86.8543 (1.0)         71.8332 (1.0)        5.2980 (1.0)         70.2937 (1.0)        0.2137 (1.0)           1;3  13.9211 (1.0)          10           1  
test_decompression_performance_1MB        262.3453 (3.80)       297.1536 (3.42)       272.5560 (3.79)      10.1432 (1.91)       268.8091 (3.82)      10.7262 (50.19)         2;1   3.6690 (0.26)         10           1  
test_compression_performance_5MB          355.2246 (5.15)       390.3580 (4.49)       364.9899 (5.08)      10.2535 (1.94)       360.8885 (5.13)       9.0850 (42.51)         1;1   2.7398 (0.20)         10           1  
test_compression_performance_10MB         724.1094 (10.50)      995.5620 (11.46)      852.1281 (11.86)     75.4677 (14.24)      850.8489 (12.10)     80.5468 (376.92)        3;0   1.1735 (0.08)         10           1  
test_decompression_performance_5MB      1,967.2563 (28.52)    2,387.8438 (27.49)    2,176.7847 (30.30)    170.0448 (32.10)    2,193.1904 (31.20)    370.7966 (>1000.0)       6;0   0.4594 (0.03)         10           1
test_decompression_performance_10MB     4,941.3552 (71.64)    6,939.9694 (79.90)    6,046.5813 (84.18)    576.4246 (108.80)   6,145.4688 (87.43)    768.6893 (>1000.0)       3;0   0.1654 (0.01)         10           1  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
```

TODO: LZW:lle suorituskykytestit (vanhalle ja uudelle?) ja lisää yleistä suorituskykytestausta 

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