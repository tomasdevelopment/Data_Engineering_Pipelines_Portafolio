================================================================ PROJECT OVERVIEW

This repository is designed to support a multi-component marketing analytics system. It includes:

A Flask application that connects to a MySQL server to store and process marketing API results.
A Streamlit dashboard that visualizes TikTok data.
A "Hogwarts DB Comparison" module that tests and compares PostgreSQL and MySQL query performance using psycopg2 and SQLAlchemy.
================================================================ REPOSITORY STRUCTURE

For clarity and maintainability, the repository is organized as follows:

/flask_app
Contains all code related to the Flask application, including the main flask_app.py file, configuration files, templates, and static assets.

/streamlit_dashboard
Contains the Streamlit TikTok dashboard code (e.g., Streamlit_tiktok_dashboard.py) and related assets.

/hogwarts_db_comparison
Contains scripts and tests for comparing PostgreSQL and MySQL performance. Subdirectories may separate PostgreSQL tests from MySQL tests.
