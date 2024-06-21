# Pytest API testing

## The project was made using Python 3.12.0

### To run the server under test in the first terminal do:
```
cd flask-api/
pip install -r requirements.txt
py -m venv .venv
source .venv/Scripts/activate
py create_db.py
py api.py
```
### To run the tests in the second terminal do:
```
cd api-tests/
pip install -r requirements.txt
py -m venv .venv
source .venv/Scripts/activate
pytest
```
