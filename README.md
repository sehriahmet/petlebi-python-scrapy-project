# petlebi-python-scrapy-project

- Extract all products from www.petlebi.com and create a JSON file. The desired attributes for the products are shown in the second line. If there are any attributes you cannot access, you can leave them blank in the JSON file.

- product URL, product name, product barcode, product price, product stock, product images, description, category, brand

- Code with 'python' while doing this 'web scraping' process. (Library to use: https://scrapy.org/)

- Write the JSON data you created to a table named 'petlebi' in a MySQL database. Again, do this step with Python.

As a result, here are the files expected in the solution:

- petlebi_scrapy.py (the py file you will write for web scraping) — when we run it, the data should be written to JSON

- petlebi_products.json (data obtained as JSON) — We should be able to see the data we print here in a Text Editor.

- import_products.py (PY file that writes from the JSON file to the petlebi table in the MySQL database) - When we run it, the data in JSON is written to the database.

- petlebi_create.sql (sql output that creates the petlebi table, hint: SQL file containing sql data starting with the CREATE statement) — When we run this, we should be able to create a table as 'petlebi' in the database

- petlebi_insert.sql (containing the SQL INSERT statements) — When we run this, we should be able to INSERT data into the table 'petlebi' where created in the previous step.
