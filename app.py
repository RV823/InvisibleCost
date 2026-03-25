from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    total_daily = 0
    monthly = yearly = message = None

    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])

        expenses.append({"name": name, "amount": amount})

    # Calculate totals
    for exp in expenses:
        total_daily += exp['amount']

    monthly = total_daily * 30
    yearly = total_daily * 365

    # Smart message
    if yearly > 50000:
        message = "🚨 Huge hidden spending!"
    elif yearly > 20000:
        message = "⚠️ This could buy something valuable!"
    else:
        message = "👍 Good control, but can improve!"

    return render_template(
        "calculator.html",
        expenses=expenses,
        total_daily=total_daily,
        monthly=monthly,
        yearly=yearly,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)