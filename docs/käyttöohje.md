

# Käyttöohje (keskeneräinen)

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
poetry run python comp_compare/main.py e <tiedoston_nimi> <algoritmi>
```

* ```e``` tarkoittaa koodausta (pakkausta),
* ```<tiedoston_nimi>``` on pakattava tiedosto (esim. ```alice.txt``` tai ```example.txt```). Voit lisätä omia .txt tiedostoja data kansioon.
* ```<algoritmi>``` voi olla joko ```huffman``` tai ```lzw```.

#### Esimerkkejä
* Huffman-koodauksella

```
poetry run python comp_compare/main.py e alice.txt huffman
``` 
* LZW-pakkauksella
```
poetry run python comp_compare/main.py e example.txt lzw
``` 
Pakatut tiedostot luodaan data kansioon tiedosto päättellä .hc jos huffman-koodauksella suoritettu tai .lzw kun LZW algoritmilla suoritettu.

### 2. Purkaminen (Decoding)

  Jos haluat purkaa pakatun tiedoston, käytä seuraavaa komentoa::
```
poetry run python comp_compare/main.py d <pakattu_tiedosto> <algoritmi>
```

* ```d``` tarkoittaa purkamista,
* ```<pakattu_tiedosto>``` on pakattu tiedosto, jonka haluat purkaa (esim. ```example.lzw``` tai ```alice.hc```),
* ```<algoritmi>``` voi olla joko ```huffman``` tai ```lzw```.

#### Esimerkkejä
* LZW-paketun tiedoston purkaminen

```
poetry run python comp_compare/main.py d example.lzw lzw
``` 



## Testien suoritus 

```
poetry run pytest
```


Suorituskykytestejä ei ajeta oletuksena, joten ne joutuu ajamaa erillisesti seuraavalla komennolla:


```
poetry run pytest --benchmark-only
```


## Testikattavuuden raportointi

```
poetry run coverage run
```