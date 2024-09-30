from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    missing_numbers = []
    result = ""
    entered_numbers = []  # List to hold entered numbers

    if request.method == 'POST':
        # Check which button was clicked
        if 'check' in request.form:
            # Collect entered numbers
            for i in range(1, 41):
                num = request.form.get(f'num{i}', '')
                if num:
                    entered_numbers.append(num)

            # Check for errors and missing numbers
            for num in entered_numbers:
                try:
                    number = int(num)
                    if number < 0 or number > 36:
                        errors.append(f"Number {number} is out of range (0-36).")
                except ValueError:
                    errors.append(f"{num} is not a valid number.")
            
            if not errors:
                all_numbers = set(range(0, 37))
                entered_set = set(map(int, entered_numbers))
                missing_numbers = sorted(all_numbers - entered_set)

                if missing_numbers:
                    result = f"Missing numbers: {', '.join(map(str, missing_numbers))}."
                else:
                    result = "No missing numbers."
        
        elif 'clear' in request.form:
            # Reset everything
            entered_numbers = []
            errors = []
            missing_numbers = []
            result = ""

    return render_template('index.html', errors=errors, result=result, missing_numbers=missing_numbers, entered_numbers=entered_numbers)

if __name__ == '__main__':
    app.run(debug=True)
