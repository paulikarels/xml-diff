# Viikkoraportti 1

## Työaika

7.5h

## Mitä olen tehnyt tällä viikolla?

Joudun vaihtamaan alkuperäisen projektin aiheen XML-Diff algoritmistä -> Lempel-Ziv-Welch (LZW) - ja Huffman-koodauksen pakentointi vertailu projektiksi.
Viikko meni päänsääntöisesti aiheen lukemisesta ja ensimmäisen Huffman-koodauksen version teossa. Projektiin on siis laadittu ensimmäinen toteutus Huffmanin koodauksesta sekä syötteen luku tiedoston pakkaamiseen/purkaamiseen (encoding & decoding). Myös pari yksenkertaista testiä luotu.

## Miten ohjelma on edistynyt?

Toteutin Huffmanin ensimmäinen toteutuksen sekä syötteen lukemisen/pakkaamisen/purkaamisen.

## Mitä opin tällä viikolla / tänään?

Opin miten tiedon pakkaus yleisesti toimii ja erityisesti miten Huffman koodaus toimii. (Vielä on epäselvyyksiä toiminnan kannalta)

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Huffmanin koodaus ja LZW algoritmit eivät ole vielä täysin tuttuja ja ongelmia oli (ja on) käyttöliittymän toteuksen kanssa, liittyen toteus tapaan.

## Mitä teen seuraavaksi?

- Luen lisää materiaalia Huffmanin koodauksesta ja korjaan mahdollisia virheitä.
- Alan työstämään ja lukemaan miten Lempel-Ziv-Welch (LZW) toimii ja tulisi toteuttaa.


## Viikon 2 Testikattavuus

Name                                        Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------------------
compression_comparison\__init__.py              0      0      0      0   100%
compression_comparison\huffman\huffman.py      59     12     18      0    77%   79-86, 92-95
tests\test_huffman.py                          19      1      2      1    90%   23
---------------------------------------------------------------------------------------
TOTAL                                          78     13     20      1    80%