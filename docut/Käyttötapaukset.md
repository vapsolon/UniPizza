# UniPizza - Käyttötapaukset

## Suunniteltu toiminnallisuus

* Mahdollisuus käyttäjän luomiseen ja kaikki tämän mukana tulevat edut kuten kanta-asiakaspisteet ja tilaustietojen helppo hakeminen
* Tilaustoiminnallisuus
* Useampaan eri osaan pilkottu menu, esim. pizzat - salaatit - juomat
* Täytteiden erottaminen omiksi olioikseen jotta pitsaan voi lisätä täytteet listalta kirjoittamisen sijasta

## Toteutettu toiminnallisuus

* Mahdollisuus käyttäjän luomiseen. Käyttäjä voi olla joko admin (oikeudet tuotteiden, täytteiden ja käyttäjien lisäämiseen, oikeudet kaiken tiedon tarkasteluun jne) tai tavallinen käyttäjä (oikeudet ruokalistan tarkasteluun ja tilaamiseen, oikeudet oman tilaushistorian tarkastelemiseen)
* Tilaustoiminnallisuus. Käyttäjä voi lisätä listalta tuotteita ostoskoriinsa ja lähettää tilauksen. Jos käyttäjä on kirjautunut palveluun, tallennetaan tilaukseen myös viite tilanneeseen käyttäjään. Myös kirjautumaton tilaaminen on mahdollista, tällöin tilauksen käyttäjäviite on **"Unregistered User"**. Kirjautumattomalta käyttäjältä kysytään tilausta varmistaessa yhteystiedot toimitusta varten, mutta näitä tietoja ei tallenneta mihinkään
* Täytteiden erottaminen omiksi olioikseen. Täytteet luodaan erikseen, ja tuotetta luodessa siihen voi lisätä täytteitä listalta ruksimalla

* Tuotteiden, täytteiden ja käyttäjien luominen admin-puolella.
* Tuotteiden ja täytteiden muokkaaminen ja poistaminen.
* Tuotteiden, täytteiden, käyttäjien ja tilauksien tarkasteleminen ylläpitäjille.

## User Storyt

* Käyttäjänä haluan tilata pitsan kotiin helposti netistä
* Käyttäjänä haluan voida tarkastella tilaushistoriaani
* Käyttäjänä haluan voida luoda oman käyttäjätilini ja täten helpottaa tilaamista entisestään
* Käyttäjänä haluan voida myös tilata kirjautumatta ja täten välttää tietojeni tallentamista pysyvään tietokantaan

## SQL-lauseet

Tilauksen lähettäminen

```INSERT INTO Order(date, price, user_id) VALUES (?, ?, ?)```

Tilaushistorian tarkastelu

```
SELECT Order.id, Order.date, Order.price, User.name, Product.name FROM Order
LEFT JOIN OrderProduct ON OrderProduct.order_id = Order.id
LEFT JOIN Product on Product.id = OrderProduct.product_id
LEFT JOIN User on User.id = Order.user_id
```

Käyttäjätilin luominen

```INSERT INTO Account(name, email, password, address, phone, admin) VALUES (?, ?, ?, ?, ?, ?)```

Kirjautumatta tilaaminen

```INSERT INTO Order(date, price, user_id) VALUES (?, ?, NULL)```