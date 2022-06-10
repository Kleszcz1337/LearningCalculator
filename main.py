from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta, date, datetime

app = Flask(__name__)
app.secret_key = "secret_key"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/", methods=["POST", "GET"])
def home():
    if(request.method == "POST"):
        session.permanent = True

        firstDate = request.form["firstDate"]
        secondDate = request.form["secondDate"]
        number = request.form["number"]

        session["Data"] = [firstDate, secondDate, number]

        sessionData = session["Data"]
        pythonDate1 = datetime.strptime(sessionData[0], '%Y-%m-%d').date()
        pythonDate2 = datetime.strptime(sessionData[1], '%Y-%m-%d').date()

        days = abs((pythonDate2 - pythonDate1).days)
        hours = days * int(number)


        flash(f"You will be learning for {days} days and it will take you {hours} hours", "info")
        return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)