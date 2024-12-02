from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Configure Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db = SQLAlchemy(app)

# Load the machine learning model
with open("model/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Define healthy ranges for plant factors
HEALTHY_RANGES = {
    "temperature": (18, 30),
    "humidity": (40, 70),
    "potassium": (100, 300),
    "ph": (5.5, 7.5),
    "nitrogen": (50, 200),
    "phosphorus": (30, 150),
}


def get_recommendations(data):
    recommendations = []
    for factor, value in data.items():
        min_val, max_val = HEALTHY_RANGES[factor]
        if value < min_val:
            recommendations.append(
                f"Increase {factor} to between {min_val} and {max_val}."
            )
        elif value > max_val:
            recommendations.append(
                f"Decrease {factor} to between {min_val} and {max_val}."
            )
    if not recommendations:
        return "All values are within the healthy range."
    return " ".join(recommendations)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    plants = db.relationship("Plant", backref="user", lazy=True)


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ph = db.Column(db.Float, nullable=False)
    nitrogen = db.Column(db.Float, nullable=False)
    phosphorus = db.Column(db.Float, nullable=False)
    potassium = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session["user_id"] = user.id
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("index"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("signup.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        username = User.query.get(session["user_id"]).username
        return render_template("dashboard.html", username=username)
    else:
        return redirect(url_for("index"))


@app.route("/analytics", methods=["GET"])
def analytics():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("analytics.html")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    if "user_id" not in session:
        return redirect(url_for("index"))

    user = User.query.get(session["user_id"])

    if request.method == "POST":
        new_username = request.form.get("new_username")
        new_password = request.form.get("new_password")

        if new_username:
            user.username = new_username
        if new_password:
            hashed_password = generate_password_hash(
                new_password, method="pbkdf2:sha256"
            )
            user.password = hashed_password

        db.session.commit()
        return redirect(url_for("dashboard"))

    return render_template("settings.html", username=user.username)


@app.route("/get_plants", methods=["GET"])
def get_plants():
    if "user_id" not in session:
        return jsonify(success=False, message="Unauthorized"), 401

    user_id = session["user_id"]
    user_plants = Plant.query.filter_by(user_id=user_id).all()

    plants = [
        {
            "id": plant.id,
            "name": plant.name,
            "ph": plant.ph,
            "nitrogen": plant.nitrogen,
            "phosphorus": plant.phosphorus,
            "potassium": plant.potassium,
            "temperature": plant.temperature,
            "humidity": plant.humidity,
        }
        for plant in user_plants
    ]
    print(f"Fetched Plants for User {user_id}: {plants}")
    return jsonify(success=True, plants=plants)


@app.route("/add_plant", methods=["POST"])
def add_plant():
    if "user_id" not in session:
        return jsonify(success=False, message="Unauthorized"), 401

    user_id = session["user_id"]
    plant_data = request.get_json()

    print(f"Received Plant Data: {plant_data}")  # Debugging: Log received data

    try:
        new_plant = Plant(
            name=plant_data["name"],
            ph=plant_data["ph"],
            nitrogen=plant_data["nitrogen"],
            phosphorus=plant_data["phosphorus"],
            potassium=plant_data["potassium"],
            temperature=plant_data["temperature"],
            humidity=plant_data["humidity"],
            user_id=user_id,
        )
        db.session.add(new_plant)
        db.session.commit()
        print(f"Plant saved: {new_plant}")  # Debugging: Log saved plant
        return jsonify(success=True)
    except Exception as e:
        print(f"Error Adding Plant: {e}")  # Debugging: Log error
        db.session.rollback()
        return jsonify(success=False, message="Error adding plant")


@app.route("/delete_plant/<int:plant_id>", methods=["DELETE"])
def delete_plant(plant_id):
    if "user_id" not in session:
        return jsonify(success=False, message="Unauthorized"), 401

    plant = Plant.query.get(plant_id)
    if not plant or plant.user_id != session["user_id"]:
        return jsonify(success=False, message="Plant not found or unauthorized"), 404

    db.session.delete(plant)
    db.session.commit()
    print(f"Deleted Plant ID: {plant_id}")
    return jsonify(success=True)


@app.route("/predict_health", methods=["POST"])
def predict_health():
    data = request.get_json()
    ph = data["ph"]
    nitrogen = data["nitrogen"]
    phosphorus = data["phosphorus"]
    potassium = data["potassium"]
    temperature = data["temperature"]
    humidity = data["humidity"]

    input_data = np.array(
        [[ph, nitrogen, phosphorus, potassium, temperature, humidity]]
    )
    prediction = model.predict(input_data)
    health_status = "Healthy" if prediction[0] == 1 else "Unhealthy"

    values = {
        "ph": ph,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "temperature": temperature,
        "humidity": humidity,
    }
    recommendations = get_recommendations(values)

    return jsonify(prediction=health_status, recommendations=recommendations)


@app.route("/help")
def help():
    if "user_id" in session:
        return render_template("help.html")
    else:
        return redirect(url_for("index"))


@app.route("/controls")
def controls():
    if "user_id" in session:
        return render_template("controls.html")
    else:
        return redirect(url_for("index"))


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user_id", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
