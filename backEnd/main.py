from flask import Flask
from src.routes.router import *
app = Flask(__name__)
loadRoutes(app)


if __name__ == "__main__":
    app.run(debug=False)