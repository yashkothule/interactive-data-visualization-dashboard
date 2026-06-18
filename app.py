from flask import (
    Flask, render_template, request,
    redirect, url_for, session, send_file
)
from io import BytesIO
import json
import pandas as pd

from flask_login import (
    LoginManager, login_user, login_required,
    logout_user, UserMixin, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

# PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# Project modules
from processing.cleaner import clean_data
from processing.visualizer import generate_dashboard
from processing.schema import detect_schema
from processing.insights import generate_insights


# ---------------- APP CONFIG ----------------
app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- LOGIN MANAGER ----------------
login_manager = LoginManager(app)
login_manager.login_view = "login"

# ---------------- DATABASE ----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="interactive_viz"
)
cursor = db.cursor(dictionary=True)

# ---------------- USER MODEL ----------------
class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    row = cursor.fetchone()
    if row:
        user = User()
        user.id = row["id"]
        return user
    return None


# ---------------- AUTH ROUTES ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (request.form["email"],)
        )
        user = cursor.fetchone()

        if user and check_password_hash(user["password"], request.form["password"]):
            u = User()
            u.id = user["id"]
            login_user(u)
            return redirect(url_for("upload"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        cursor.execute(
            "INSERT INTO users (username,email,password) VALUES (%s,%s,%s)",
            (
                request.form["username"],
                request.form["email"],
                generate_password_hash(request.form["password"])
            )
        )
        db.commit()
        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- DASHBOARD ----------------
@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    charts = []
    figures = []
    kpis = {}
    insights = []
    filters_data = {}
    data_loaded = False

    # -------- Handle CSV Upload --------
    if request.method == "POST" and "file" in request.files:
        file = request.files["file"]
        if file:
            df = pd.read_csv(file)
            df = clean_data(df)
            session["csv_data"] = df.to_json(date_format="iso")

    # -------- Load CSV from Session --------
    if "csv_data" in session:
        df = pd.read_json(session["csv_data"])
        data_loaded = True

        # Detect schema
        schema = detect_schema(df)

        # Build dynamic filters
        filters_data = {
            col: sorted(df[col].dropna().unique())
            for col in schema["categorical"]
        }

        # Applied filters
        applied_filters = {
            k: v for k, v in request.form.items()
            if v and k in df.columns
        }

        # Generate dashboard
        charts, kpis, figures = generate_dashboard(df, **applied_filters)

        # Generate insights
        insights = generate_insights(df)

        # Save dashboard snapshot
        cursor.execute(
            """
            INSERT INTO dashboards
            (user_id, dashboard_name, filters_json, data_json)
            VALUES (%s,%s,%s,%s)
            """,
            (
                current_user.id,
                f"Dashboard {pd.Timestamp.now()}",
                json.dumps(applied_filters),
                session["csv_data"]
            )
        )
        db.commit()

    return render_template(
        "upload.html",
        charts=charts,
        kpis=kpis,
        insights=insights,
        filters=filters_data,
        data_loaded=data_loaded
    )


# ---------------- EXPORT PDF ----------------
@app.route("/export-pdf", methods=["POST"])
@login_required
def export_pdf():

    if "csv_data" not in session:
        return redirect(url_for("upload"))

    df = pd.read_json(session["csv_data"])

    applied_filters = {
        k: v for k, v in request.form.items()
        if v and k in df.columns
    }

    _, kpis, figures = generate_dashboard(df, **applied_filters)

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 40
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, y, "Dashboard Report")

    pdf.setFont("Helvetica", 11)
    y -= 30

    for key, value in kpis.items():
        pdf.drawString(40, y, f"{key}: {value}")
        y -= 15

    y -= 20

    for fig in figures:
        img_buf = BytesIO()
        fig.write_image(img_buf, format="png", width=700, height=450)
        img_buf.seek(0)

        if y < 300:
            pdf.showPage()
            y = height - 40

        pdf.drawImage(
            ImageReader(img_buf),
            40,
            y - 250,
            width=520,
            height=250,
            preserveAspectRatio=True,
            mask="auto"
        )
        y -= 270

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="dashboard.pdf",
        mimetype="application/pdf"
    )


# ---------------- LOGOUT ----------------
@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("login"))


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
