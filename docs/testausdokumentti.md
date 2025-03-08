# Testausdokumentti

### Miten testataan

Projektin testaus perustuu päänsääntöisesti toiminnallisuuteen katettaviin yksikkötesteihin, jotka testaavat valtaosin pakkaamis ja purku vaiheen. 
Huffmanin-koodauksessa testataan myös laajemmin sen apufunktioiden toimintaa merkkijono syötteillä, kun taas LZW:n testit pohjautuvat pelkästään tiedoston lukuun, pakkaamiseen ja purkuun.

Testidata on jaettu kahteen eri ryhmään perustestidataan ja suorituskykydataan.
Perustestidata sisältää "geneerisiä" tilanteita jotka pohjautuvat mahdollisiin tilanteisiin tuotannossa (tyhjät syötteet, erikoismerkit, jne). 
Suorituskykydata koostuu suuri kokoisista tiedostoista jotka koostuvat numeroista.

Testejä suorittaessa testisuorituksien tulokset (tiedostot) luodaan data\test_results kansioon testattavan tiedoston nimellä ja sen käytettävllä algoritmillä "hc" tai "lzw".

---

### Yksikkötestit

Valtaosa projektin testeistä on yksikkötesteja, joiden pohja kohdistuu kaiikke luokille ja metodeille, poislukien pieniä poikkeuksia.

### Testisyötteet

LZW- ja Huffman-algoritmit voivat toimia eri tavoin riippuen syötteiden koosta ja sisällöstä, testisyötteet koostuvat erikokoisista ja -sisältöisistä .txt-tiedostoista. 
Tällä hetkellä Unit-testien tekstisyötteet kattavat seuraavat:
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
Name                                 Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------------------
comp_compare\__init__.py                 0      0      0      0   100%
comp_compare\huffman\__init__.py         0      0      0      0   100%
comp_compare\huffman\compressor.py      14      0      6      0   100%
comp_compare\huffman\encoding.py        36      0     18      0   100%
comp_compare\huffman\tree.py            25      0      6      0   100%
comp_compare\huffman\utils.py           23      1     10      1    94%   8
comp_compare\lzw\bitio.py               70     11     22      2    84%   5-6, 22-29, 68-69
comp_compare\lzw\constants.py            4      0      0      0   100%
comp_compare\lzw\decoding.py            23      0     10      0   100%
comp_compare\lzw\dictionary.py           7      0      2      0   100%
comp_compare\lzw\encoding.py            28      0      8      0   100%
comp_compare\lzw\trie.py                28      0     10      1    97%   32->28
--------------------------------------------------------------------------------
TOTAL                                  258     12     92      4    95%
```

---

### Kompressiotestit

Kompressiotestit testaavat Huffman-koodauksen ja LZW algoritmien pakkaustehoa, jossa käydään 4 erilaista tiedostoa yksi kerrallaan läpi. Tiedostot pakataan ensin, sitten verrataan niiden kokoa alkuperäisiin ja lopuksi ne puretaan varmistaakseen, että purku/pakkausprosessi toimii oikein

Testit voidaan suorittaa esimerkiksi seuraavalla komennolla, joka printtaa myös testitulokset:

```
poetry run pytest -s .\tests\compression_tests\
```

Saatu tulokset:
```
tests\compression_tests\huffman_compress_decompress_test.py File: alice.txt
 Original size: 170.26 KB
 Compressed size: 92.91 KB
 Compression ratio: 45.43% smaller

.File: random_text.txt
 Original size: 976.56 KB
 Compressed size: 582.04 KB
 Compression ratio: 40.40% smaller

.File: redundancy.txt
 Original size: 0.04 KB
 Compressed size: 0.03 KB
 Compression ratio: 35.71% smaller

.File: small_text_1MB.txt
 Original size: 1026.26 KB
 Compressed size: 442.43 KB
 Compression ratio: 56.89% smaller

.
tests\compression_tests\lzw_compress_decompress_test.py  File: alice.txt
 Original size: 170.26 KB
 Compressed size: 83.74 KB
 Compression ratio: 50.82% smaller

.File: random_text.txt
 Original size: 976.56 KB
 Compressed size: 679.28 KB
 Compression ratio: 30.44% smaller

.File: redundancy.txt
 Original size: 0.04 KB
 Compressed size: 0.06 KB
 Compression ratio: -54.76% smaller

.File: small_text_1MB.txt
 Original size: 1026.26 KB
 Compressed size: 477.50 KB
 Compression ratio: 53.47% smaller
```

---

### Suorituskykytestit
Suorituskykytestien ajamiseen menee tällä useampi minuutti (20~, LZW:n takia), joista saadan vastaa raportti (Zoomaa ulos tarvittaessa):

```
poetry run pytest .\tests\performance_tests\ --benchmark-only
```

```
----------------------------------------------------------------------------------------------------------- benchmark: 10 tests -----------------------------------------------------------------------------------------------------------
Name (time in ms)                                        Min                     Max                    Mean                StdDev                  Median                   IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_huffman_compression_performance_1MB             99.2615 (1.0)          119.9008 (1.0)          106.4331 (1.0)         11.6716 (inf)          100.1371 (1.0)         15.4795 (inf)           1;0  9.3956 (1.0)           3           1
test_huffman_decompression_performance_1MB          235.1892 (2.37)         242.5974 (2.02)         237.9318 (2.24)         4.0612 (inf)          236.0089 (2.36)         5.5561 (inf)           1;0  4.2029 (0.45)          3           1
test_huffman_compression_performance_5MB            416.4343 (4.20)         510.0318 (4.25)         463.4281 (4.35)        46.8000 (inf)          463.8182 (4.63)        70.1981 (inf)           1;0  2.1578 (0.23)          3           1
test_huffman_compression_performance_10MB           842.3623 (8.49)       1,009.7378 (8.42)         901.4716 (8.47)        93.8932 (inf)          852.3148 (8.51)       125.5316 (inf)           1;0  1.1093 (0.12)          3           1
test_huffman_decompression_performance_5MB        1,669.9291 (16.82)      1,769.7369 (14.76)      1,705.3495 (16.02)       55.8544 (inf)        1,676.3825 (16.74)       74.8559 (inf)           1;0  0.5864 (0.06)          3           1
test_lzw_decompression_performance_1MB            3,451.3066 (34.77)      3,608.8412 (30.10)      3,505.8840 (32.94)       89.2174 (inf)        3,457.5043 (34.53)      118.1509 (inf)           1;0  0.2852 (0.03)          3           1
test_huffman_decompression_performance_10MB       4,445.0914 (44.78)      5,186.8452 (43.26)      4,799.6392 (45.10)      371.9537 (inf)        4,766.9811 (47.60)      556.3153 (inf)           1;0  0.2083 (0.02)          3           1
test_lzw_compression_performance_1MB              6,861.3984 (69.12)      9,178.4150 (76.55)      8,262.4042 (77.63)    1,232.2973 (inf)        8,747.3993 (87.35)    1,737.7624 (inf)           1;0  0.1210 (0.01)          3           1
test_lzw_decompression_performance_5MB           18,362.3885 (184.99)    18,362.3885 (153.15)    18,362.3885 (172.53)       0.0000 (1.0)       18,362.3885 (183.37)       0.0000 (1.0)           0;0  0.0545 (0.01)          1           1
test_lzw_compression_performance_5MB            846,790.1368 (>1000.0)  846,790.1368 (>1000.0)  846,790.1368 (>1000.0)      0.0000 (1.0)      846,790.1368 (>1000.0)      0.0000 (1.0)           0;0  0.0012 (0.00)          1           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

Kaikkia testikokoja mitä suorituskykydatasta löytyi (15MB, 20MB, 40MB) ei testattu suurien suoritusajojen takia.