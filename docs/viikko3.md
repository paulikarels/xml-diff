# Viikkoraportti 1

## Työaika

13-17h

## Mitä olen tehnyt tällä viikolla?

Sain aikaiseksi ensimmäisen version LZW-purkaus/pakkaus -algoritmista. Sen tulisi toimia (ja sainkin tiedoston purettua ja pakattua), mutta siinä voi olla kumminkin vielä hiettovaa/bugeja.
Myös huffmanin-koodaus tulisi olla mielästäni nyt valmis. Sain siihen rakenettua nyt Huffman-puun tiedostoon ja rakenettua päätestejä suurien tiedostojen kanssa. LZW:stä vielä sain tehtyä testin ja siihen bittiluku luokan toiminnallisuutta varten.

## Miten ohjelma on edistynyt?

Huffman-koodaus on mielestäni valmis, vain testien teko puuttuu. Myös LZW on mielestäni hyvällä tahdilla saatu käyntiin.

## Mitä opin tällä viikolla / tänään?

Päänsääntöisesti opin miten LZW-pakkaus ja -purku toimii ja myös aika paljon vianetsintää ja tuontivirheiden korjausta pythonilla.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

LZW:n bitti käsittely toi vaikeuksia ja on vielä vaikea täysin ymmärtää sen toiminnallisuutta, löysin stackoverflowsta bitreader/bitwriterin jota olen hyödyntänyt, joka myös toi vaikeuksia LZW:n luonnin kannalta. 

## Mitä teen seuraavaksi?

- Viimeistelen LZW-purkaus/pakkaus -algoritmia tarpeen mukaan
- Lisää testejä (tiedostonkoko vertaus, suorituskyky, päätoiminnalisuus, jne)