from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Likith@1719",
    database="lead_management"
)

cursor = db.cursor()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    business = request.form["business"]
    message = request.form["message"]

    sql = """
    INSERT INTO leads(name,email,phone,business_type,message)
    VALUES(%s,%s,%s,%s,%s)
    """

    values = (name, email, phone, business, message)

    cursor.execute(sql, values)

    db.commit()

    return "Data Inserted Successfully"


if __name__ == "__main__":
    app.run(debug=True)