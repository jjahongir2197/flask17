from flask import Flask, render_template, request

app = Flask(__name__)

students = []

@app.route("/", methods=["GET", "POST"])
def grades():

    if request.method == "POST":

        name = request.form["name"]
        grade = int(request.form["grade"])

        if grade >= 90:
            result = "A"

        elif grade >= 80:
            result = "B"

        elif grade >= 70:
            result = "C"

        else:
            result = "F"

        students.append({
            "name": name,
            "grade": grade,
            "result": result
        })

    return render_template(
        "index.html",
        students=students
    )

if __name__ == "__main__":
    app.run(debug=True)
