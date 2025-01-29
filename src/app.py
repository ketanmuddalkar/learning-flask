from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello World!"


@app.route("/success/<int:score>")
def success(score: int):
    return "The person has passed and the marks is " + str(score)


@app.route("/fail/<int:score>")
def fail(score: int):
    return "The person has failed and the marks is " + str(score)


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


if __name__ == "__main__":
    app.run(debug=True)
