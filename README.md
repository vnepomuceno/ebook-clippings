# E-book Clippings

![Build Status](https://api.travis-ci.com/vnepomuceno/ebook-clippings.svg?branch=master)

## Getting Started

Checkout project and run:

```bash
poetry install
```

## Commands

### Convert `My Clippings.txt` to a `.json` file

```bash
poetry run import --input-filepath="resources/2021-10-27-MyClippings.txt" --output-filepath="resources/clippings.json"
```