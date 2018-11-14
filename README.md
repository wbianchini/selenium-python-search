# Selenium with python - google search example

Selenium webdriver bot to perform a google search by given input data and parse all results to a file

According to [Wikipedia](https://en.wikipedia.org/wiki/Selenium_(software)), Selenium is a portable software-testing framework for web applications. Selenium provides a playback tool for authoring tests without the need to learn a test scripting language. 

## Usage

GoogleMe class will look for a json file called input_data.json on root folder 
This file must contain a valid json with "google-me" index list

The results of a search will be displayed in a output.json file as a json on the root folder 

GoogleMe uses geckodriver to perform search as default. 
You must have geckodriver on your environment to run this package

To run GoogleMe test session, you must execute the following command
```sh
python3 -m src
```

### Tests

All testes are on the "/tests" folder
This package has pytest as requirement.

To run all tests, you must execute pytest from the root folder
```sh
python3 -m pytest tests
```