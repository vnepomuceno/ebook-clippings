# E-book Clippings

[![Build Status](https://app.travis-ci.com/vnepomuceno/ebook-clippings.svg?branch=main)](https://app.travis-ci.com/vnepomuceno/ebook-clippings)

## Getting Started

Checkout project and run:

```bash
▶ poetry install
```

## Commands

### Convert `My Clippings.txt` to a `.json` file

```bash
▶ poetry run import --input-filepath="resources/2021-10-27-MyClippings.txt" --output-filepath="resources/clippings.json"
```

## Run Django app

```bash
▶ poetry run python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 08, 2022 - 17:42:37
Django version 4.0.1, using settings 'app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```