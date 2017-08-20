# ABCD Bank

A credit card validation from ABCD Bank.

A valid credit card from ABCD Bank has the following characteristics:

- It must start with a 4, 5 or 6. 
- It must contain exactly 16 digits. 
- It must only consist of digits (0-9). 
- It may have digits in groups of 4, separated by one hyphen "-". 
- It must NOT use any other separator like ' ' , '_', etc. 
- It must NOT have 4 or more consecutive repeated digits.

# Steps to run

Clone the repository and using your virtualenv, run the following steps on terminal:

1. pip install -r requirements.txt
2. export FLASK_APP=app_creditcard/app_creditcard.py
3. export FLASK_DEBUG=true
4. flask run

This project is deployed on Heroku: [https://anchor-loans-test.herokuapp.com/](https://anchor-loans-test.herokuapp.com/)

