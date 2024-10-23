# rule-engine-as
# rule-engine-ast

- **Application_1/**: Main project folder containing all core files.
- **app.py**: Main Python script where the Flask application logic is implemented.
- **templates/**: Folder that stores all HTML files.
- **index.html**: The main HTML file rendered by Flask.
- **static/**: Folder that stores static files like CSS and JavaScript.
- **style.css**: Stylesheet defining the look and feel of the web app.
- **script.js**: JavaScript file for client-side interactivity.

## How to Run
1. **Install Dependencies**:
   - Ensure Python and Flask are installed.
   - You can install Flask using pip:
     ```bash
     pip install Flask
     ```

2. **Run the Application**:
   - Navigate to the project directory and run the Flask application:
     ```bash
     python app.py
     ```

3. **Access the Application**:
   - Open a web browser and go to the URL displayed in the terminal (typically `http://127.0.0.1:5000/`).
   - Input a rule, age, income, and department in the provided form, then submit to see if the rule passes or fails.

## Technical Details
- **Frontend**: HTML and CSS are used for the user interface. Users input rules and data via a form on the web page.
- **Backend**: Python Flask serves as the backend framework, handling rule parsing, validation, and evaluation.
- **AST-based Evaluation**: The rule string is parsed into an AST (Abstract Syntax Tree), ensuring structured and safe evaluation of the rule.

## Limitations
1. **Limited Rule Syntax**: Supports basic rules with AND/OR operators. Advanced conditions or nested logic (e.g., parentheses) are not supported.
2. **Error Handling**: Error messages are generated for invalid syntax or attributes but may not always provide detailed information.
3. **No Persistent Rule Storage**: Currently, rules are not stored or saved. Users must input new rules each time.

## Feature Improvements
1. **Enhanced Rule Syntax**: Support for more advanced conditions, such as nested logical conditions and functions.
2. **Persistent Rule Storage**: Implement persistent storage to allow users to save and reuse rules.
3. **Advanced Error Handling**: Improve the clarity and detail of error messages to assist users in debugging their rules.
4. **Extended Attributes**: Allow for more flexible attributes in the rules (e.g., percentages, decimals, and dynamically defined attributes).

## Conclusion
The Rule Engine Application provides a user-oriented interface for creating rules and evaluating them against user-defined conditions. It demonstrates fundamental techniques in rule parsing and validation using Flask and Python's AST. This project serves as a foundation for building more complex rule-based systems, particularly in decision-making applications.
