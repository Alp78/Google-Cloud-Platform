from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\alexi\\Documents\\GCP_Python\\restapibooks\\books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False