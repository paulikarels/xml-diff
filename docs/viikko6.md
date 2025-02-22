# Viikkoraportti 6

## Työaika

noin 9-12h.

## Mitä olen tehnyt tällä viikolla?

Paljon refaktorointia Huffmanille ja LZW:lle, jotta se olisi luettavampaa ja helpommin ylläpidettävää (+ testien muokkaus niiden ympärille). LZW:lle siirsin Trie-puurakenteen (aijemmin oli kaksi LZW:stä) päätoiminnalisuudeksi ja muokkasin testejä sen ympärille. 
Myös paljon parannuksia/korjauksia dokumentaatioon, komentojen suoritukseen ja testien toimintaan ennen toista vertaisarviointia.

## Miten ohjelma on edistynyt?

Ohjelma on mielestäni toiminnallisesti valmis. Saatan lisätä ennen viimeistä palautusta yksinkertaisen käyttöliittymän, joka selkeyttää komentojen käyttöä, esimerkiksi  --help-komennon ja paremmin jäsennellyt ohjeet sinne. Muuten ohjelman tulisi olla valmis – ellei  bugeja ilmene.

## Mitä opin tällä viikolla / tänään?

Kuinka hidas LZW on Huffman-koodaukseen verrattuna, kun syötteissä ei ole pajon toistoa, jolloin sen sanakirjan rakentaminen vie enemmän aikaa.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Ei epäselvyyksiä.

## Mitä teen seuraavaksi?

- Viimeistelyjä lopullista palautusta varten ja vertaisarvioinnin palautteen hyödyntämistä
- Teen toisen testidata vertailun jossa olisi enenmmän toistettavaa tietoa, jossa voitaisiin nähdä LZW:n hyötyjä.
- Muuta viimeistelyä/hiomista.
