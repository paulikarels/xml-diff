# Määrittelydokumentti

## Ohjelmointikieli

Projektin teen Pythonilla. Pystyn vertaisarvioida Pythonilla, Javalla, C#:lla ja JavaScriptillä tehtyjä projekteja. 

## Algoritmit ja tietorakenteet

Projektin ideana on vertailla Lempel-Ziv-Welch (LZW) - ja Huffman-koodauksen pakkausmenetelmiä tiedostojen pakkaamisessa. 

LZW-pakkausalgoritmi perustuu toistuvien merkkijonojen löytämiseen ja korvaamiseen lyhyimmillä koodilla (bitillä). Algoritmi ei vaadi etukäteen tietoa merkkien esiintymisistä, vaan se luo  symbolitaulukon (tai tietorakenteen) pakkausprosessin aikana.

Huffman-koodaus puolestaan perustuu siihen, kuinka usein kukin merkki esiintyy tiedostossa. Sen avulla luodaan puurakenne, jossa yleisemmin esiintyville symboleille annetaan lyhyemmät bitit ja harvemmin esiintyville pidemmät. 

Tiivistetysti: LZW keskittyy toistuvien merkkijonojen esiintymiseen, kun taas Huffman perustuu yksittäisten merkkien esiintymiskertojen määrään.

## Ongelma

Ongelma, jonka yritän ratkaista, liittyy Lempel-Ziv-Welch (LZW) ja Huffman-koodauksen vertailuun tiedostojen pakkaamisessa. Tavoitteena on tutkia, kumpi menetelmä tarjoaa paremman pakkaussuhteen ja suorituskyvyn.  

## Syötteet

Ohjelma ottaa syötteeksi pakattuja tai pakkaamattomia tiedostoja/tekstiä.

## Aika- ja tilavaativuudet


Huffman koodauksen aikavaativuus on O(n log n + m), jossa n vastaa merkkien määrää ja m syötteen määrää. Rajoittavana tekijänä on siis merkkien ja kääntämisen määrän/laskemisen kannalta.


## Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti (TKT).

## Kieli

Dokumentaatiot on suomeksi ja ohjelmakoodi englanniksi.

## Viitteet
- [1] https://research.cs.wisc.edu/niagara/papers/xdiff.pdf
- [2] https://docs.python.org/3/library/xml.etree.elementtree.html
