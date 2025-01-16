# Määrittelydokumentti

## Ohjelmointikieli

Projektin teen Pythonilla. Pystyn vertaisarvioida Pythonilla, Javalla, C#:lla ja JavaScriptillä tehtyjä projekteja.

## Algoritmit ja tietorakenteet

Projektin ideana on luoda XML-Diff algoritmi (luultavasi X-Diff) [1], joka on suunniteltu XML-dokumenttien muutosten havaitsemiseen. Syy miksi luultavasti menen X-Diff algoritmillä enkä esimerkiksi Zhang-Shasha-puumuutos algoritmilla on se että X-Diff ottaa huomioon XML-dokumenttien ominaisuudet, kuten solmujen järjestyksen ja mahdolliset liikkeet hierarkiassa. Algoritmi siis luo muutosoperaatioiden sarjan (edit scriptin) muutoksista.

XML-Diff algorithim toteukseen tulen käyttämään XML-dokumentteja kuvaavaa puutietorakennetta 
[2]. XML-dokumentit ovat luonteeltaan hierarkkisia, joten ne esitetään puina, joissa jokainen solmu vastaa yhtä XML-elementtiä. Eli projektissa käytän Pythonin 
xml.etree.ElementTree-kirjastoa XML-dokumenttien parsimiseen ja puiden luomiseen. 

## Ongelma

Ongelma, jonka yritän ratkaista, liittyy XML-dokumenttien rakenteellisten eroavaisuuksien tunnistamiseen. Tavoitteenani on luoda ohjelma, joka vertailee kahta XML-dokumenttia ja niiden muutoksia (lisäykset, poistot, päivitykset ja solmujen siirrot). XML-dokumenttien hierarkkinen rakenne tekee tämän haasteelliseksi, sillä perinteiset tekstipohjaiset diff-työkalut eivät pysty käsittelemään rakenteellisia muutoksia oikein.

Ideana olisi luoda XML-Diff algoritmi (luultavasi X-Diff) ratkaisemaan tämä ongelma, koska se tunnistaa tarkasti solmujen liikkeet ja muutokset puun rakenteessa.

## Laskennallinen vaativuus



## Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti (TKT).

## Kieli

Dokumentaatiot on suomeksi ja ohjelmakoodi englanniksi.


## Viitteet
- [1] https://research.cs.wisc.edu/niagara/papers/xdiff.pdf
- [2] https://docs.python.org/3/library/xml.etree.elementtree.html
