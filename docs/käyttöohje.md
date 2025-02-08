

# Käyttöohje (keskeneräinen)

Ohjel

## Vaatimukset

- Python 3.10
- poetry 2.0

## Asennus
```
poetry install
```

## Suoritus

### 1. Koodaus (Encoding)

  Jos haluat pakata tiedoston, käytä seuraavaa komentoa:
```
poetry run python compression_comparison/main.py e <tiedoston_nimi> <algoritmi>
```

* ```e``` tarkoittaa koodausta (pakkausta),
* ```<tiedoston_nimi>``` on pakattava tiedosto (esim. ```alice.txt``` tai ```example.txt```). Voit lisätä omia .txt tiedostoja data kansioon.
* ```<algoritmi>``` voi olla joko ```huffman``` tai ```lzw```.

#### Esimerkkejä
* Huffman-koodauksella

```
poetry run python compression_comparison/main.py e alice.txt huffman
``` 
* LZW-pakkauksella
```
poetry run python compression_comparison/main.py e example.txt lzw
``` 
Pakatut tiedostot luodaan data kansioon tiedosto päättellä .hc jos huffman-koodauksella suoritettu tai .lzw kun LZW algoritmilla suoritettu.

#### Huomio:
Tiedosto alice.txt on erittäin suuri, joten se saattaa viedä aikaa käsitellä. Jos käytät LZW-pakkausta, kannattaa luoda oma pienempi tekstitiedosto data kansioon kokeilua varten.

### 2. Purkaminen (Decoding)

  Jos haluat purkaa pakatun tiedoston, käytä seuraavaa komentoa::
```
poetry run python compression_comparison/main.py d <pakattu_tiedosto> <algoritmi>
```

* ```d``` tarkoittaa purkamista,
* ```<pakattu_tiedosto>``` on pakattu tiedosto, jonka haluat purkaa (esim. ```example.lzw``` tai ```alice.hc```),
* ```<algoritmi>``` voi olla joko ```huffman``` tai ```lzw```.

#### Esimerkkejä
* LZW-paketun tiedoston purkaminen

```
poetry run python compression_comparison/main.py d example.lzw lzw
``` 



## Testien suoritus (keskeneräinen)

```
poetry run pytest
```



## Testikattavuuden raportointi

```
poetry run coverage run
```