# Toteutusdokumentti

## Ohjelman rakenne

### Huffmanin koodaus

Projektini toteustus Huffman-koodauksesta perustuu binääripuun ja minimikekon (min-heap) käyttöön. Huffmanin puurakenne toteuteaan heapq-moduliin minikekoa hyödyntäen laskien merkkien esiintymismäärän/tiheyden, jossa pinemmät solmut yhdistetään kunnes saamme valmiin puun. Luonti prosessi perustuu läpikäymällä binaaripuuta josta muodostetaan sanakirja (Huffman-koodit), jolloin annetaan jokaiselle merkille bittikoodit. Tämän jälkeen sanakirjaa ei talleneta suoraan   vaan se serialisoidaan, jotta voimme purkaa ilman erillistä sanakirjan tallennusta. Lopuksi binäärinen merkkijono muunnetaan tavuiksi compress()-funkkarilla, jossa lisätään tarvittaessa täytebittejä ja pakattu muutetaan takaisin binääriseksi merkkijonoksi decompress()-funktiolla. Lopuksi puramme deserialize_tree()-funkkarilla HUffmanin-puun serialisoinnin ja palautamme tiedoston alkuperäiseen muotoon.


### LZW (Lempel-Ziv-Welch)

TODO.


### Aikavaativuus

Huffmanin koodauksen aikavaativuus on O(n+m log m), jossa m on uniikkien merkkien määrä ja n syötteen merkkien määrä. 

TODO: Tarkennusta aikavaativuuksiin + LZW