from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    result = None
    if request.method == "POST":
       try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
       except ValueError:
         error = "Пожалуйста, введите корректные числа."
         return render_template('index.html', error=error)

       if operation == "add":
           result = num1 + num2
       elif operation == "subtract":
           result = num1 - num2
       elif operation == "multiply":
           result = num1 * num2
       elif operation == "divide":
           if num2 == 0:
              error = "Деление на ноль!"
              return render_template('index.html', error=error)
           result = num1 / num2

       return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)