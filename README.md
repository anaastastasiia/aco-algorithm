# Ant Colony Optimization for Traveling Salesman problem

## Description
This is a web application that uses the Ant Colony Optimization (ACO) algorithm to solve the Traveling Salesman problem (TSP). The application allows for the visualization of the best-found solution as a graph, as well as displaying detailed results such as the order of visited cities and the total length of the path.

## Ant Colony Optimization (ACO)

Ant Colony Optimization (ACO) is a probabilistic technique inspired by the behavior of ants foraging for food. The algorithm involves a number of artificial ants searching for an optimal solution by iteratively constructing paths and updating pheromone levels on paths they traverse. The pheromone levels guide subsequent ants toward shorter paths.

### Key Components

- **Pheromone Matrix**: Represents the pheromone levels on each edge (city-to-city connection). Initially, all edges have the same pheromone value, which is updated over time.
  
- **Ants**: A set of artificial ants that explore the cities and construct solutions. Each ant starts at a random city and chooses the next city based on pheromone levels and distances.
  
- **Transition Probability**: The probability \( P(i \to j) \) of moving from city `i` to city `j` is determined by the pheromone level and the inverse of the distance:
  \[
  P(i \to j) = \frac{{\tau(i, j)^\alpha \cdot \eta(i, j)^\beta}}{{\sum_{k \in C} \tau(i, k)^\alpha \cdot \eta(i, k)^\beta}}
  \]
  where:
  - \( \tau(i, j) \) is the pheromone level on edge \( (i, j) \).
  - \( \eta(i, j) = \frac{1}{D(i, j)} \) is the desirability or inverse of the distance.
  - \( \alpha \) and \( \beta \) control the influence of pheromone and distance.

- **Pheromone Update**: After all ants complete their tours, pheromone levels are updated based on the path quality:
  \[
  \tau(i, j) = (1 - \rho) \cdot \tau(i, j) + \Delta \tau(i, j)
  \]
  where \( \rho \) is the pheromone evaporation rate, and \( \Delta \tau(i, j) \) is the pheromone deposited by ants.

### Parameters

- **Number of ants (`num_ants`)**: The number of ants exploring the solution space.
- **Number of iterations (`num_iterations`)**: The number of iterations the algorithm will run.
- **Alpha (`α`)**: Controls the importance of pheromone in the decision-making process.
- **Beta (`β`)**: Controls the influence of the distance on the decision-making process.
- **Rho (`ρ`)**: The pheromone evaporation rate.
  
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
