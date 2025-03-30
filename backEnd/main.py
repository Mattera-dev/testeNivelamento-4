from flask import Flask
from flask_cors import CORS
from src.routes.router import *
app = Flask(__name__)
loadRoutes(app)
CORS(app)


if __name__ == "__main__":
    app.run(debug=False)