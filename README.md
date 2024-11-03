# Data To CSV API
Api to transform data into csv format. We use some resources to get this possible. This project is build with [Python](https://www.python.org/) programming language and its technologies.

Here at this documentation we attached each lib link or required service, then you can check by yourself.

## Summary

1. [Description](#description)
2. [Dependencies](#dependencies)
3. [How To Run?](#how-to-run)
   1. [Testing](#testing)
4. [Structure](#structure)
5. [Routes](#routes)

## Description
This project has the intent of transform data or files into a CSV format. Mainly datatypes or files that can be transformed into tables, which is the main purpose of a CSV format.

We have our routes [here](#routes) with its description and expected data type, be by text or by file.

This software integrates some Python technologies to become that possible, see more about it in [dependencies](#dependencies) section, (the next).

## Dependencies
Here you can see the list of the dependencies installed at this project using the library [Pip](https://pypi.org/).

*This project is build using **Python**, so I recommend you have the Python3.10 or greater installed.*

> Dependencies List:

* [FastAPI](https://fastapi.tiangolo.com/);
* [PyTest](https://docs.pytest.org/en/stable/);
* [PyTest Async](https://pytest-asyncio.readthedocs.io/);
* [Pandas](https://pandas.pydata.org/);
* [Python DotEnv](https://github.com/theskumar/python-dotenv);

**NOTE: to install all dependencies, I strongly recommend you run the following commandline:**

```commandline
pip install -r requirements.txt
```

## How To Run?
These are the instructions to run our application. You can do it using some commands options like:

* By FastAPI:
```commandline
fastapi run app.py
```

* By Python File Directly:
```commandline
python app.py
```
Note: some python installations need you to run the command `python3 app.py` to run.

### Testing
You can use your **IDE** Graphic Interface to run the tests, but if you prefer, you can just type at your terminal:

```commandline
pytest
```

Then, you can verify if your tests are working or not.

## Structure
Here you can find the package's project structure:

```text
src/
├──controllers/
├──core/
├──exceptions/
├──prototypes/
├──routes/
├──services/
├──use_cases/
├──utilities/
tests/
├──mocks/
├──src/
├──├──core/
├──├──routes/
├──├──services/
├──├──utilities/
.gitignore
app.py
LICENSE
README.md
```

## Routes
At this section, I present you all HTTP requests routes for this project.

| Method | Route URL | Description | Request                                              |
|--------|-----------|-------------|------------------------------------------------------|
| POST   | /api/v1/json-csv/file | Transform an object list to csv file format | [json to csv](docs/RequestBody.md#json-to-csv-route) |

That's all Folks!
[Go Ahead](#data-to-csv-api)
