document.getElementById('ruleForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from refreshing the page

    const rule = document.getElementById('rule').value;
    const age = document.getElementById('age').value;
    const income = document.getElementById('income').value;
    const department = document.getElementById('department').value;

    // Create the data to send to the server
    const data = {
        rule: rule,
        attributes: {
            age: parseInt(age),
            income: parseInt(income),
            department: department
        }
    };

    // Send the POST request to the server
    fetch('/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        let outputDiv = document.getElementById('output');
        if (result.error) {
            // Display the error message
            outputDiv.innerHTML = `<p style="color:red;">Error: ${result.error}</p>`;
        } else {
            // Display the result message
            outputDiv.innerHTML = `<p style="color:green;">Rule result: ${result.result ? "Passed" : "Failed"}</p>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
