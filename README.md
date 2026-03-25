# InvisibleCost
As a college student, I built this project to solve a common problem—untracked daily expenses. People often spend without realizing how small costs add up. This tool helps track spending, identify unnecessary expenses, and improve savings by making invisible costs visible.




I built Invisible Cost using HTML and CSS for a modern, interactive frontend and Python (Flask) for backend logic.
The application takes daily expenses as input, stores them, and performs calculations to determine total spending.
The core logic is based on simple calculations:
Monthly Expense = Daily Expense × 30
Yearly Expense=Daily Expense×365
The results are then dynamically displayed using Flask templates, along with smart insights that show how small expenses grow over time.
languages used html,css,python,flask



InvisibleCost/
│── app.py
│── templates/
│     ├── index.html
│     └── calculator.html
│── static/
      └── style.css
