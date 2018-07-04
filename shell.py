import os
from app import app, db
from app.models import CarPart, load_part

os.environ["PYTHONINSPECT"] = "True"
