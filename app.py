from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from aco_algorithm import AntColony
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def load_distance_matrix(csv_file):
    data = pd.read_csv(csv_file, header=None, on_bad_lines='skip')
    data.columns = ['ID', 'X', 'Y']
    coordinates = data[['X', 'Y']].values

    def euclidean_distance(coord1, coord2):
        return np.linalg.norm(coord1 - coord2)

    num_cities = len(coordinates)
    distance_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

    return distance_matrix.astype(float)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_algorithm', methods=['POST'])
def run_algorithm():
    num_ants = int(request.form['num_ants'])
    num_iterations = int(request.form['num_iterations'])
    alpha = float(request.form['alpha'])
    beta = float(request.form['beta'])
    rho = float(request.form['rho'])

    distances = load_distance_matrix('data/berlin52.csv') 

    aco = AntColony(distances, num_ants, num_iterations, alpha, beta, rho)
    best_path, best_length = aco.solve()

    best_path = [int(x) for x in best_path]  
    best_length = float(best_length) 

    img = io.BytesIO()
    plot_best_path(distances, best_path)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode('utf8')

    return jsonify({
        'best_path': best_path,
        'best_length': best_length,
        'graph_url': graph_url
    })

def plot_best_path(distances, best_path):
    x = distances[:, 0]
    y = distances[:, 1]

    plt.figure(figsize=(10, 8))
    plt.scatter(x, y, color='blue', s=100, label='Miasta')  
    plt.plot(x[best_path], y[best_path], color='red', linewidth=2, label='Najlepsza ścieżka') 

    for i, (city_x, city_y) in enumerate(zip(x, y)):
        plt.text(city_x + 5, city_y + 5, str(i), fontsize=12, color='black')

    plt.title("Najlepsza droga do rozwiązania problemu komiwojażera", fontsize=16)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)


if __name__ == '__main__':
    app.run(debug=True)
