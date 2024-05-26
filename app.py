import os
import sqlite3
import dash
import dash_bootstrap_components as dbc
from flask_login import  UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  create_engine
from app import *
from models import Sector, Users

estilos = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    dbc.themes.MINTY,
]
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
)

conn = sqlite3.connect("./src/database/database.db")
engine = create_engine("sqlite:///src/database/database.db")
db = SQLAlchemy()

app = dash.Dash(
    __name__,
    external_stylesheets=estilos + [dbc_css],
)
server = app.server
app.config.suppress_callback_exceptions = True
app.title = "MES Tork tomadas de força"

server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI="sqlite:///src/database/database.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db.init_app(server)
