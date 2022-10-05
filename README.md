# ObrasPublicas


# Project description

This project allows establishing a basic CRUD application which allows storing data or pre-established templates for all the documentation used.
Additionally, each template has associated attached files which are stored directly in the server files system, and their path is stored in the database. 
These files can also be uploaded, downloaded and modified.

The project is built using python and the framework Flask, as a database we are using a SQL (any) database using a SQLAlchemy ORM using the extension provided 
by flask  [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/).
Bootstrap is being used as CCS framework using Flask-Bootstrap Flask Extension.


The project is divided into different python packages, or more technically flask blueprints.

# Modules

- Main (Dashboard)
- Errors (http error handler)
- Auth (authenticator module)
- InventarioVial (to store the information made in road inventory)
- Hautomotor (resume and documentation of machinery and vehicles)
- HVObra (resume and documentation of the construction works carried out)
- PQRS (management and assignment of suggestions, issues, claims or complaints)

There are some classes associated to modules that are related to classes of other objects, for instance: some PQRS can be related to some road (InventoryVial class-model) or some construction site (HojaObra class-model).

## 
