from flask import Flask
from flask import redirect
from flask import url_for

from webapp.views.data_as import data_as

app = Flask(__name__)

@app.get("/")
def index():
    return redirect(url_for("data_as.index"))
    
    
def create_app(enviroment):
    app.config.from_object(enviroment)

    app.register_blueprint(data_as)

    return app