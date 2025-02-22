# Toteutusdokumentti

## Ohjelman rakenne

Lyhyesti: Ohjelma mahdollistaa tiedostojen pakkaamisen käyttäen kahta eri algoritmia: Huffman-koodaus ja LZW-pakkaus (Lempel–Ziv–Welch). Käyttäjä suorittaa ohjelman komentoriviltä ja antaa sille tiedoston sekä haluamansa pakkausalgoritmin.

### Huffmanin koodaus

Projektini toteustus Huffman-koodauksesta perustuu binääripuun ja minimikekon (min-heap) käyttöön. Huffmanin puurakenne toteuteaan heapq-moduliin minikekoa hyödyntäen laskien merkkien esiintymismäärän/tiheyden, jossa pinemmät solmut yhdistetään kunnes saamme valmiin puun. Luonti prosessi perustuu läpikäymällä binaaripuuta josta muodostetaan sanakirja (Huffman-koodit), jolloin annetaan jokaiselle merkille bittikoodit. Tämän jälkeen sanakirjaa ei talleneta suoraan   vaan se serialisoidaan, jotta voimme purkaa ilman erillistä sanakirjan tallennusta. Lopuksi binäärinen merkkijono muunnetaan tavuiksi compress()-funkkarilla, jossa lisätään tarvittaessa täytebittejä ja pakattu muutetaan takaisin binääriseksi merkkijonoksi decompress()-funktiolla. Lopuksi puramme deserialize_tree()-funkkarilla HUffmanin-puun serialisoinnin ja palautamme tiedoston alkuperäiseen muotoon.


### LZW (Lempel-Ziv-Welch)

LZW-pakkauksen toteutus perustuu Trie-puurakenteeseen, johon lisätään merkkijonoja pakkausprosessin aikana. Alussa sanakirjassa on kaikki yksittäiset merkit, jonka jälkeen etsitään pisin mahdollinen merkkijono joka löytyy sanakirjasta. Tämän merkkijonon koodi kirjoitetaan pakattuun tiedostoon BitWriter-luokan avulla. Tämän jälkeen uusi merkkijono lisätään sanakirjaan, ja jos se ei vielä ole siellä, prosessia jatketaan kunnes kaikki merkit on käsitelty/lisätty.

Purkamisessa taas käytetään samaa sanakirjaa, jota luetaan BitReader-luokan avulla, jossa jokainen koodi käännetään takaisin vastaavaksi merkkijonoksi. Kun koodi on purettu, uusi merkkijono lisätään sanakirjaan yhdistämällä aiemmin purettu merkkijono ja seuraavan merkkijonon ensimmäinen merkki. Tätä jatketaan, kunnes koko tiedosto on purettu takaisin alkuperäiseen muotoonsa.

Vielä lisäyksenä, algoritmi käyttää siis BitReader- ja BitWriter-luokkia bittien lukemiseen ja kirjoittamiseen **tehokkuuden parantamiseksi**.



### Aikavaativuus

Huffmanin koodauksen aikavaativuus on O(n+m log m), jossa m on uniikkien merkkien määrä ja n syötteen merkkien määrä. 

LZW-algoritmin aikavaativuus koostuu pakkamisesta (encoding) ja purkamisesta (decode). Koska LZW käyttää  Trie-puuta, Trie-rakenteessa hakeminen ja lisääminen vievät O(m) aikaa, jossa m on merkkijonon pituus. Koska pakkaus käsittelee jokaisen tiedoston merkin kerran, koko prosessin aikavaativuus on O(n * m), missä n on tiedoston merkkimäärä. Mutta m on melko pieni vakio, koska Trie-puun merkkijonot eivät kasva liian pitkiksi, jolloin voimme sanoa likimääräisesti aikavaativuuden olaven O(n).
