================================================================ PROJECT OVERVIEW

This repository is designed to support a python sql quering of different sql engies as mysql, postgres sql and redshift, using a wide variety of Python libraries. It includes:

A Flask application that connects to a MySQL server to store and process marketing API results.
A Streamlit dashboard that visualizes TikTok data.
A "Hogwarts DB Comparison" module that tests and compares PostgreSQL and MySQL query performance using psycopg2 and SQLAlchemy.
================================================================ REPOSITORY STRUCTURE

For clarity and maintainability, the repository is organized as follows:

/Flaskapp+Streamlit_tiktok_dashboard.py
Contains the Streamlit TikTok dashboard code (e.g., Streamlit_tiktok_dashboard.py) and related assets.
& also contains all code related to the Flask application, including the main flask_app.py file, configuration files, templates, and static assets.

/hogwarts_db_comparison
Contains scripts and tests for comparing PostgreSQL and MySQL performance. Subdirectories may separate PostgreSQL tests from MySQL tests.
