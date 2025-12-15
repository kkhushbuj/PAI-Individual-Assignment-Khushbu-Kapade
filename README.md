# PAI-Individual-Assignment-Khushbu-Kapade

## Source Code Overview

The project follows a modular Python-based structure to ensure clarity, maintainability, and separation of concerns. Each module is responsible for a specific aspect of the system.

## Author

**Khushbu Kapade**  
Individual Assignment

## Task 1 - The project is implemented entirely in Python and follows a modular design (Branch: main-task1):

- **User Interface:** Streamlit-based web interface for interacting with public health data, generating records, viewing statistics, and visualising trends.
- **Data Management Layer:** SQLite-based persistence layer for storing, updating, and deleting public health records.
- **Data Generation Module:** Synthetic data generation logic used to create realistic public health records without relying on external APIs or CSV datasets.
- **Analytics Module:** Summary statistics and trend analysis for key public health metrics.
- **Testing:** Test-Driven Development (TDD) approach using PyTest to validate data generation, database operations, and analytical functionality.

## Task 2 – Market Basket Analysis Using Statistical Methods (Branch: main-task2)

### Description
Task 2 focuses on analysing supermarket transaction data to uncover purchasing relationships between products.  
The task is implemented using statistical association techniques rather than graphical visualisation or machine learning approaches.

The system evaluates transaction data using **support**, **confidence**, and **lift** metrics to identify meaningful product associations and generate interpretable recommendations.

### Key Features

- Statistical analysis using support, confidence, and lift
- Deterministic and explainable recommendation logic
- Console-based output for clarity and reproducibility
- Test-Driven Development (TDD) using PyTest


