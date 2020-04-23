# UniPizza - Käyttötapaukset

## Suunniteltu toiminnallisuus

* Mahdollisuus käyttäjän luomiseen ja kaikki tämän mukana tulevat edut kuten kanta-asiakaspisteet ja tilaustietojen helppo hakeminen
* Tilaustoiminnallisuus
* Useampaan eri osaan pilkottu menu, esim. pizzat - salaatit - juomat
* Täytteiden erottaminen omiksi olioikseen jotta pitsaan voi lisätä täytteet listalta kirjoittamisen sijasta

## Toteutettu toiminnallisuus

* Mahdollisuus käyttäjän luomiseen. Käyttäjä voi olla joko admin (oikeudet tuotteiden, täytteiden ja käyttäjien lisäämiseen, oikeudet kaiken tiedon tarkasteluun jne) tai tavallinen käyttäjä (oikeudet ruokalistan tarkasteluun ja tilaamiseen)
* Tilaustoiminnallisuus. Käyttäjä voi lisätä listalta tuotteita ostoskoriinsa ja lähettää tilauksen. Jos käyttäjä on kirjautunut palveluun, tallennetaan tilaukseen myös viite tilanneeseen käyttäjään. Myös kirjautumaton tilaaminen on mahdollista, tällöin tilauksen käyttäjäviite jätetään vain tyhjäksi. Kirjautumattomalta käyttäjältä ei tosin vielä kysytä mitään tietoja, joten tilaus jää toimittamatta.
* Täytteiden erottaminen omiksi olioikseen. Täytteet luodaan erikseen, ja tuotetta luodessa siihen voi lisätä täytteitä listalta ruksimalla.

* Tuotteiden, täytteiden ja käyttäjien luominen admin-puolella.
* Tuotteiden ja täytteiden muokkaaminen ja poistaminen.
* Tuotteiden, täytteiden, käyttäjien ja tilauksien tarkasteleminen ylläpitäjille.

## User Storyt

* Käyttäjänä haluan tilata pitsan kotiin helposti netistä
* Käyttäjänä haluan voida tukea vakiopaikkaani kanta-asiakkaana ja saada tätä kautta myös pieniä etuja itselleni
* Käyttäjänä haluan voida tarkastella tilaushistoriaani
* Käyttäjänä haluan voida luoda oman käyttäjätilini ja täten helpottaa tilaamista entisestään