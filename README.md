# UoMCanvasScraper

A tool to scrape course materials from a Canvas instance

## Usage

> [!NOTE]
> current work in progress

- Install all dependencies using `pip install .`
- Run `python3 src/main.py`
- Enter initial desired directory

> [!NOTE]
> potential for this file to store structure? (e.g. folder per subject)

- This will be stored for later usages

## Contributing

### Precommit

- This repository makes use of the [pre-commit](https://pre-commit.com/) library to ensure coding standards
- Install it using the command `pre-commit install`

### Github actions

- When creating a merge request, a Github action will trigger to test the pull request
- This could fail due to a faulty test, ensure you check that as well

## Milestones

- [ ] Get api endpoint working
- [ ] Have a cli tool to organise pdfs
  - [x] Select from downloads directory
- [ ] Graphical front end to organise pdfs
