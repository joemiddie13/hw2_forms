@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        Also, enter a topping:<br>
        <input type="text" name="topping"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_topping = request.args.get('topping')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with {users_froyo_topping} as a topping!'


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    first_number = int(request.args.get('operand1'))
    second_number = int(request.args.get('operand2'))
    user_math_selection = request.args.get('operation')
    if user_math_selection == 'add':
        result = first_number + second_number
        operation = "add"
        symbol = "+"
    elif user_math_selection == 'subtract':
        result = first_number - second_number
        operation = "subtract"
        symbol = "-"
    elif user_math_selection == 'multiply':
        result = first_number * second_number
        operation = "multiply"
        symbol = "*"
    elif user_math_selection == 'divide':
        result = first_number / second_number
        operation = "divide"
        symbol = "/"
    return f"You chose to {operation} {first_number} {symbol} {second_number}. Your result is: {result}"