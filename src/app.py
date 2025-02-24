from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/success/<int:score>")
def success(score: int):
    return render_template("results.html")


@app.route("/fail/<int:score>")
def fail(score: int):
    return render_template("results.html")


@app.route("/results/<int:score>")
def results(score: int):
    """
    This function is a score checker.

    if score > 50:
        send to success
    else:
        send to fail
    """

    result = ""

    if score < 50:
        result = "fail"
    else:
        result = "success"

    return redirect(url_for(result, score=score))


@app.route("/submit", methods=["POST", "GET"])
def submit():
    """
    This function will display html page for the results.
    """

    total_score = 0

    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c_prog = float(request.form["c"])
        datascience = float(request.form["datascience"])

        total_score = (science + maths + c_prog + datascience) / 4

    res = ""
    if total_score >= 50:
        res = "success"
    else:
        res = "fail"

    return redirect(url_for(res, score=total_score))


if __name__ == "__main__":
    app.run(debug=True)
