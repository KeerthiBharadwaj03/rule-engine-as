from flask import Flask, render_template, request, jsonify
import ast

app = Flask(__name__)

# Home route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Safely evaluate a rule using the Abstract Syntax Tree (AST)
def evaluate_rule(rule, attributes):
    # Define allowed variable names for the rule
    allowed_names = {
        'age': attributes.get('age'),
        'income': attributes.get('income'),
        'department': attributes.get('department', '')
    }

    try:
        # Ensure the rule is stripped of any leading/trailing whitespace
        rule = rule.strip()

        # Replace any logical operators written in words (like AND, OR) with their Python equivalents
        rule = rule.replace("AND", "and").replace("OR", "or")

        # Parse the rule into an AST (Abstract Syntax Tree)
        node = ast.parse(rule, mode='eval')

        # Ensure only valid nodes (safe operations) are allowed
        for subnode in ast.walk(node):
            if not isinstance(subnode, (ast.Expression, ast.BinOp, ast.BoolOp, ast.Compare, ast.Name, ast.Load, 
                                        ast.And, ast.Or, ast.Gt, ast.GtE, ast.Lt, ast.LtE, ast.Eq, ast.Num)):
                return {"error": "Invalid rule syntax or unsafe operation detected."}

        # Safely evaluate the rule with allowed variables only
        compiled = compile(node, '<string>', 'eval')
        result = eval(compiled, {"__builtins__": None}, allowed_names)
        return {"result": result}

    except SyntaxError as se:
        return {"error": f"Invalid syntax: {se}"}
    except Exception as e:
        return {"error": str(e)}

# Route to handle rule submission
@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.get_json()

    rule = data.get('rule')
    attributes = data.get('attributes')

    # Validate the input attributes
    if not rule or not attributes.get("age") or not attributes.get("income"):
        return jsonify({"error": "Invalid input. Rule, Age, and Income are required."}), 400

    # Evaluate the rule and return the result
    result = evaluate_rule(rule, attributes)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
