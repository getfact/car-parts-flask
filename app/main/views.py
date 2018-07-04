from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import CarPart
from app.main.forms import PostForm
from app.main import bp

@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    form = PostForm()
    if form.validate_on_submit():
        part = CarPart(name=form.name.data, body=form.body.data)
        db.session.add(part)
        db.session.commit()
        flash("Your Post Is Live!")
        return redirect(url_for("main.index"))

    parts = CarPart.query.all()
    return render_template("index.html", title="Home", form=form, parts=parts)

@bp.route("/about")
def about():
    return render_template("about.html", title="About")
