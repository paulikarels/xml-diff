# Toteutusdokumentti

## Ohjelman rakenne

Ohjelma mahdollistaa tiedostojen pakkaamisen käyttäen kahta eri algoritmia: Huffman-koodaus ja LZW-pakkaus (Lempel–Ziv–Welch). Käyttäjä suorittaa ohjelman komentoriviltä ja antaa sille tiedoston sekä haluamansa pakkausalgoritmin.

### Huffmanin koodaus

Projektini toteustus Huffman-koodauksesta perustuu binääripuun ja minimikekon (min-heap) käyttöön. Huffmanin puurakenne toteuteaan heapq-moduliin minikekoa hyödyntäen laskien merkkien esiintymismäärän/tiheyden, jossa pinemmät solmut yhdistetään kunnes saamme valmiin puun. Luonti prosessi perustuu läpikäymällä binaaripuuta josta muodostetaan sanakirja (Huffman-koodit), jolloin annetaan jokaiselle merkille bittikoodit. Tämän jälkeen sanakirjaa ei talleneta suoraan   vaan se serialisoidaan, jotta voimme purkaa ilman erillistä sanakirjan tallennusta. Lopuksi binäärinen merkkijono muunnetaan tavuiksi compress()-funkkarilla, jossa lisätään tarvittaessa täytebittejä ja pakattu muutetaan takaisin binääriseksi merkkijonoksi decompress()-funktiolla. Lopuksi puramme deserialize_tree()-funkkarilla HUffmanin-puun serialisoinnin ja palautamme tiedoston alkuperäiseen muotoon.

### LZW (Lempel-Ziv-Welch)

LZW-pakkauksen toteutus perustuu Trie-puurakenteeseen, johon lisätään merkkijonoja pakkausprosessin aikana. Alussa sanakirjassa on kaikki yksittäiset merkit, jonka jälkeen etsitään pisin mahdollinen merkkijono joka löytyy sanakirjasta. Tämän merkkijonon koodi kirjoitetaan pakattuun tiedostoon BitWriter-luokan avulla. Tämän jälkeen uusi merkkijono lisätään sanakirjaan, ja jos se ei vielä ole siellä, prosessia jatketaan kunnes kaikki merkit on käsitelty/lisätty.

Purkamisessa taas käytetään samaa sanakirjaa, jota luetaan BitReader-luokan avulla, jossa jokainen koodi käännetään takaisin vastaavaksi merkkijonoksi. Kun koodi on purettu, uusi merkkijono lisätään sanakirjaan yhdistämällä aiemmin purettu merkkijono ja seuraavan merkkijonon ensimmäinen merkki. Tätä jatketaan, kunnes koko tiedosto on purettu takaisin alkuperäiseen muotoonsa.

Vielä lisäyksenä, algoritmi käyttää siis BitReader- ja BitWriter-luokkia bittien lukemiseen ja kirjoittamiseen **tehokkuuden parantamiseksi**. 

### Aikavaativuus

Huffmanin koodauksen aikavaativuus on O(n+m log m), jossa m on uniikkien merkkien määrä ja n syötteen merkkien määrä. 
Log m tulee siitä, että Huffman-puu rakennetaan prioriteettijonon avulla, mikä vaatii logaritmisen ajan suhteessa uniikkien merkkien määrään. 

LZW-algoritmin aikavaativuus koostuu pakkamisesta (encoding) ja purkamisesta (decode). Koska LZW käyttää  Trie-puuta, Trie-rakenteessa hakeminen ja lisääminen vievät O(m) aikaa, jossa m on merkkijonon pituus. Koska pakkaus käsittelee jokaisen tiedoston merkin kerran, koko prosessin aikavaativuus on O(n * m), missä n on tiedoston merkkimäärä. Mutta m on melko pieni vakio, koska Trie-puun merkkijonot eivät kasva liian pitkiksi, jolloin voimme sanoa likimääräisesti aikavaativuuden olaven O(n).

###  Kielimallien käyttö

Kielimalleja tuli käytettyä algoritmien ja muiden asioiden ymmärtämiseksi ja selvittämiseksi. 
Tuotin/Höydinsin kyllä kielimalleja säätääkseen filtteröintiä/sääntöjä komennoille (esim. "poetry run pytest .\tests\performance_tests\ --benchmark-only"), jotka löytyvät tiedostoista: conftest.py, .coveragerc ja pytest.ini. 


## Viitteet
-  https://en.wikipedia.org/wiki/Huffman_coding
-  https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
-  https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
-  https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
