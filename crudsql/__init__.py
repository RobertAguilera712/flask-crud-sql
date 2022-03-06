import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

PASSWORD = os.getenv('SQL_CRUD_PASSWORD')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bb1131c414ecf54fbcb5ff9253dbff52'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://uptavhrw2wcpvvzj:{PASSWORD}@bp1hcse6uzd0yftvypzh-mysql.services.clever-cloud.com:3306/bp1hcse6uzd0yftvypzh'
db = SQLAlchemy(app)

from crudsql import routes
