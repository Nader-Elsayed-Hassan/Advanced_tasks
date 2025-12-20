from flask import Flask, render_template, request, redirect, session, flash, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"
DB_NAME = "database.db"

def get_db():
    return sqlite3.connect(DB_NAME)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        c = conn.cursor()

        c.execute("SELECT COUNT(*) FROM users")
        user_count = c.fetchone()[0]

        role = "admin" if user_count == 0 else "user"

        c.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role)
        )
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        c = conn.cursor()
        c.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        user = c.fetchone()
        conn.close()

        if user:
            session["user"] = user[1]
            session["role"] = user[3]

            if session["role"] == "admin":
                return redirect("/admin")
            else:
                return redirect("/user")

    return render_template("login.html")


@app.route("/admin")
def admin():
    if "user" not in session or session.get("role") != "admin":
        return redirect("/login")

    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()

    return render_template("admin.html", users=users)

@app.route("/delete/<int:user_id>")
def delete_user(user_id):
    if "user" not in session or session.get("role") != "admin":
        return redirect("/login")

    conn = get_db()
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()

    return redirect("/admin")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
@app.route("/user")
def user_page():
    if "user" not in session or session.get("role") != "user":
        return redirect("/login")

    return render_template("user.html", username=session["user"])

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    flash("✅ Your message was sent successfully!", "success")
    return redirect(url_for("user_page"))


if __name__ == "__main__":
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

    app.run(debug=True)
