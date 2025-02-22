# Testausdokumentti

### Miten testataan

Projektin testaus perustuu päänsääntöisesti toiminnallisuuteen katettaviin yksikkötesteihin. Suorituskykytestejä en ole vielä tehnyt, mutta nekin tulevat tehtyä myöhemmin. Myös aion lisätä lisää perustoiminnallisuustestejä ja ehkä integraatiotestejä käyttöliittymän testaamiseksi.


### Yksikkötestit

Valtaosa projektin testeistä on yksikkötesteja, joiden pohja kohdistuu kaiikke luokille ja metodeille, poislukien pieniä poikkeuksia.

### Integraatiotestit

TODO: ?

### Suorituskykytestit
Suorituskykytestien ajamiseen menee tällä useampi minuutti (20~, LZW:n takia), joista saadan vastaa raportti (Zoomaa ulos tarvittaessa):

```
--------------------------------------------------------------------------------------------------------- benchmark: 10 tests ----------------------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                       Max                      Mean              StdDev                    Median                   IQR            Outliers     OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_compression_performance_1MB              116.3159 (1.0)            124.6640 (1.0)            119.4058 (1.0)        4.5770 (inf)            117.2376 (1.0)          6.2611 (inf)           1;0  8.3748 (1.0)           3           1
test_decompression_performance_1MB            168.1877 (1.45)           170.6245 (1.37)           169.7332 (1.42)       1.3437 (inf)            170.3874 (1.45)         1.8276 (inf)           1;0  5.8916 (0.70)          3           1
test_compression_performance_5MB              557.0660 (4.79)           563.4272 (4.52)           560.7237 (4.70)       3.2862 (inf)            561.6780 (4.79)         4.7709 (inf)           1;0  1.7834 (0.21)          3           1
test_compression_performance_10MB           1,101.5147 (9.47)         1,253.3442 (10.05)        1,152.1798 (9.65)      87.6110 (inf)          1,101.6805 (9.40)       113.8721 (inf)           1;0  0.8679 (0.10)          3           1
test_decompression_performance_5MB          1,382.8930 (11.89)        1,525.2333 (12.23)        1,448.2814 (12.13)     71.8712 (inf)          1,436.7179 (12.25)      106.7552 (inf)           1;0  0.6905 (0.08)          3           1
test_decompression_performance_1MB          1,921.3888 (16.52)        2,367.1170 (18.99)        2,095.2926 (17.55)    238.4528 (inf)          1,997.3720 (17.04)      334.2962 (inf)           1;0  0.4773 (0.06)          3           1
test_decompression_performance_10MB         4,395.1405 (37.79)        5,146.9097 (41.29)        4,658.1859 (39.01)    423.6594 (inf)          4,432.5074 (37.81)      563.8269 (inf)           1;0  0.2147 (0.03)          3           1
test_compression_performance_1MB            8,015.0899 (68.91)        9,626.2652 (77.22)        8,777.0955 (73.51)    809.1166 (inf)          8,689.9314 (74.12)    1,208.3815 (inf)           1;0  0.1139 (0.01)          3           1
test_decompression_performance_5MB         11,419.3837 (98.18)       11,419.3837 (91.60)       11,419.3837 (95.64)      0.0000 (1.0)         11,419.3837 (97.40)        0.0000 (1.0)           0;0  0.0876 (0.01)          1           1
test_compression_performance_5MB        1,194,213.9077 (>1000.0)  1,194,213.9077 (>1000.0)  1,194,213.9077 (>1000.0)    0.0000 (1.0)      1,194,213.9077 (>1000.0)      0.0000 (1.0)           0;0  0.0008 (0.00)          1           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Testisyötteet

LZW- ja Huffman-algoritmit voivat toimia eri tavoin riippuen syötteiden koosta ja sisällöstä, testisyötteet koostuvat erikokoisista ja -sisältöisistä .txt-tiedostoista. 
Tällä hetkellä tekstisyötteet kattavat seuraavat:
- **Tyhjät syötteet**, eivät siis sisällä mitään.
- **Lyhyet tekstit**, sisältävät yksinkertaisia ja toistuvia merkkejä.
- **Pitkät tekstit**, laajempi sanakirja ja enemmän erikoismerkkejä tai muita harvinaisempia merkkejä.
- **Erilaiset merkistöt**, kuten aakkoset, numerot ja erikoismerkit, jne.



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
Name                                 Stmts   Miss  Cover   Missing
------------------------------------------------------------------
comp_compare\__init__.py                 0      0   100%
comp_compare\huffman\__init__.py         0      0   100%
comp_compare\huffman\compressor.py      14      0   100%
comp_compare\huffman\encoding.py        36      0   100%
comp_compare\huffman\tree.py            25      3    88%   23, 28-29
comp_compare\huffman\utils.py           23      3    87%   8, 25, 27
comp_compare\lzw\bitio.py               70     11    84%   5-6, 22-29, 68-69
comp_compare\lzw\constants.py            4      0   100%
comp_compare\lzw\decoding.py            23      0   100%
comp_compare\lzw\dictionary.py           7      0   100%
comp_compare\lzw\encoding.py            28      0   100%
comp_compare\lzw\trie.py                28      0   100%
------------------------------------------------------------------
TOTAL                                  258     17    93%
```