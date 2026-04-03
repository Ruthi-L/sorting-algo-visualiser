from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate_array():
    # Generates a random array of 20 integers
    data = random.sample(range(10, 100), 20)
    return jsonify(data)

@app.route('/bubble-sort/<data>')
def bubble_sort(data):
    # Converts string back to list of ints
    arr = [int(x) for x in data.split(',')]
    steps = []
    n = len(arr)
    
    # Core Algorithmic Logic: Bubble Sort
    # We record each swap as a 'step' for the frontend to visualize
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(list(arr)) # Record the state of the array
    
    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
