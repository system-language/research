# app.py

from flask import Flask, render_template, request, jsonify
from simulator import run_simulation


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    # Extract data from the request
    data = request.json
    user_count = float(data['user_count'])
    transaction_fee = float(data['transaction_fee'])
    marketing_effort = float(data['marketing_effort'])
    regulatory_env = int(data['regulatory_env'])


    # Run the simulation
    user_counts, fee_revenues = run_simulation(10, user_count, transaction_fee, marketing_effort, regulatory_env)

    # Return the results as JSON
    return jsonify({"user_counts": user_counts, "fee_revenues": fee_revenues})

if __name__ == '__main__':
    app.run(debug=True)


