# petlebi-python-scrapy-project

- Extracting all products from www.petlebi.com and create a JSON file. The desired attributes for the products are shown in the second line.

- product URL, product name, product barcode, product price, product stock, product images, description, category, brand

- Coded with 'python' while doing this 'web scraping' process. (Library to use: https://scrapy.org/)

- Writing the JSON data which is created to a table named 'petlebi' in a MySQL database. Again, doing this step with Python.

As a result, here are the files expected in the solution:

- petlebi_scrapy.py (the py file which is written for web scraping)

- petlebi_products.json (data obtained as JSON)

- import_products.py (PY file that writes from the JSON file to the petlebi table in the MySQL database) - When we run it, the data in JSON is written to the database.

- petlebi_create.sql (sql output that creates the petlebi table, hint: SQL file containing sql data starting with the CREATE statement) — When we run this, we should be able to create a table as 'petlebi' in the database

- petlebi_insert.sql (containing the SQL INSERT statements) — When we run this, we should be able to INSERT data into the table 'petlebi' where created in the previous step.
