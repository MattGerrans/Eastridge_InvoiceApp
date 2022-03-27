# Simple Invoice App for Eastridge interview challenge

## Usage:

Clone the project.

In the project directory, run `python manage.py runserver`

Using a tool like [PostMan](https://www.postman.com/downloads/), you can post Invoices to `http://127.0.0.1:8000/invoice/`
Here is sample data for posting an invoice: `{"created_date": "2001-01-01"}``


Once you have created an Invoice, you can create InvoiceItems for it under its ID, eg. `http://127.0.0.1:8000/invoice/1/`
Here is sample data for creating an InvoiceItem: `{"units": "parsec", "description": "Cosmological data", "amount": 3.26}`

From a browser, you can get Invoices at  `http://127.0.0.1:8000/invoice/` and see InvoiceItems for an Invoice at `http://127.0.0.1:8000/invoice/[ID]/`

## Administration
To access the administration, set up your user name and password by running `py manage.py createsuperuser`

Then you can access the administration pages under the `admin/` pages, which will allow you to do additional things that were not coded into the application, like delete entries.

## Notes
There is sample data in the database already. This is just to make it a little easier to view things before adding any data. In a production system, the database would start out empty (or populated from some legacy system).


