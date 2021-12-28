from flask import Flask
from flask_pymongo import PyMongo
import string
import secrets

app = Flask(__name__)

app.secret_key = ''.join(secrets.choice(string.ascii_uppercase + string.digits)for i in range(28))

# app.config['MONGO1_URI'] = "mongodb+srv://ajayvardhanreddy:ajayvardhan@learnmongo.dba5m.mongodb.net/learnpymongo?retryWrites=true&w=majority"
app.config['MONGO_URI'] = "mongodb+srv://ajayvardhanreddy:ajayvardhan@learnmongo.dba5m.mongodb.net/portfolio?retryWrites=true&w=majority"


mongo = PyMongo(app)
users_accounts_col = mongo.db.portfolioaccounts
portfolio_details_col = mongo.db.portfoliodetails






