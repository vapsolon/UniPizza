# UniPizza - Tietokantarakenne

![Tietokantakaavio](https://vapsolon.github.io/UniPizza/docut/Tietokantakaavio.png)

## SQL-lauseet

```
CREATE TABLE account(
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	email VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	address VARCHAR(144) NOT NULL, 
	phone VARCHAR(144) NOT NULL, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id),
)

CREATE TABLE ingredient(
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE product(
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	price FLOAT NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE productingredient(
	product_id INTEGER, 
	ingredient_id INTEGER, 
	FOREIGN KEY(product_id) REFERENCES product (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredient (id)
)

CREATE TABLE order(
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	date DATE NOT NULL, 
	price FLOAT NOT NULL, 
	user_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id)
)

CREATE TABLE order_product(
	date_created DATETIME, 
	date_modified DATETIME, 
	id INTEGER NOT NULL, 
	order_id INTEGER, 
	product_id INTEGER, 
	amount INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(order_id) REFERENCES order (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
)
```