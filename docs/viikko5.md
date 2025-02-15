# Viikkoraportti 5

## Työaika

noin 8-9h.

## Mitä olen tehnyt tällä viikolla?

Paransin LZW-algoritmia käyttämällä Trie puurakennetta, mikä nopeutti hakua erittäin paljon ja uusien merkkijonojen lisäystä verrattuna vanhaan sanakirjapohjaiseen menetelmään (Dictionary). Laadin myös suorituskykytestejä (päänsääntöisesti Huffmanille) sekä testejä tiedoston kokoon liittyen (onko pienempi eli "compressoitu"). Myös ensimmäinen vertaisarviointi tehtiin, sekä sain palautetta jossa ehdotettiin merkkijono syötettä tiedostojen lisäksi.Mieluiten jätän projektin kohdistumaan tiedostoihin pakkaamiseen, purkamiseen sekä algoritmien suorituksien vertaamiseen tiedosto syötteillä, enkä ala nyt "sooloilemaan" merkkijonosyötteiden kanssa vaikka se ei olisi suuri homma.  

## Miten ohjelma on edistynyt?

Ohjelman tulisi olla valmis LZW ja Huffmanin-koodauksen kannalta. Testejä luotu ja ainoa asia mitä voisi parantaa (ja ollaan parantamassa) on LZW:n suorituskyky.
Pitää kumminkin vielä muokata entinen LZW toimimaan Trie puurakenteella (ei pitäisi olla iso homma), sillä tällä hetkellä Trie puurakenteinen (tehty) ja sanakirjapohjainen toimivat erillisesti. 

## Mitä opin tällä viikolla / tänään?

Suorituskykytestien teosta ja Trie puurakenteesta hieman.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Ei epäselvyyksiä.

## Mitä teen seuraavaksi?

- Muokkaan vanhan LZW toimimaan Trie puurakenteen kanssa (mietin kannataisiko vanha jättää esimerkkinä, vaikka se on 50x hitaampi?). Tein jo toimivian Trie puurakenteen joka toimi suorituskykytesteissä, mutta voi löytyä kumminkin muutama bugi tai virhe unit testeissä kun vaihdan Trie puurakenteeseen, joita korjailen.
- Lisään uusia unit/yksikkö- ja suorituskykytestejä LZW:lle kun saan Trie puurankentee siirrettyä.
- Pieniä sekalaisia korjauksia/hiontaa ennen toista vertaisarvointia.
