# Ant Colony Optimization for Traveling Salesman problem

## Description
This is a web application that uses the Ant Colony Optimization (ACO) algorithm to solve the Traveling Salesman problem (TSP). The application allows for the visualization of the best-found solution as a graph, as well as displaying detailed results such as the order of visited cities and the total length of the path.

## Ant Colony Optimization (ACO)

Ant Colony Optimization (ACO) is a probabilistic technique inspired by the behavior of ants foraging for food. The algorithm involves a number of artificial ants searching for an optimal solution by iteratively constructing paths and updating pheromone levels on paths they traverse. The pheromone levels guide subsequent ants toward shorter paths.
  
## Technologies
- **Python**: The main backend technology.
- **Flask**: Web framework for building the backend application.
- **Ant Colony Optimization (ACO)**: The algorithm used to solve the Traveling Salesman Problem.
- **Matplotlib**: Library for generating visualizations.
- **HTML, CSS, JavaScript**: Frontend technologies.
- **Bootstrap**: CSS framework for building a responsive user interface.

## Installation

### Prerequisites
To run this project, you need to have:
- Python 3.6 or higher
- pip (Python Package Installer)

### Installation steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/tsp-aco.git
2. **Install required dependencies**:
   ```bash
   pip install flask numpy pandas
3. **Train the model by running**:
   ```bash
   python aco_algorithm.py
4. **Run the application**:
   ```bash
   python app.py
5. **Open your browser and navigate to**:
   ```bash
   http://127.0.0.1:5000
