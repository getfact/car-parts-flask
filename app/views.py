from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import PostForm
from app.models import CarPart

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = PostForm()
    if form.validate_on_submit():
        part = CarPart(name=form.name.data, body=form.body.data)
        db.session.add(part)
        db.session.commit()
        flash("Your Post Is Live!")
        return redirect(url_for("index"))

    parts = CarPart.query.all()
    return render_template("index.html", title="Home", form=form, parts=parts)
