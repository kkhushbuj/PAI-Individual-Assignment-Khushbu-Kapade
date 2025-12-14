# PAI-Individual-Assignment-Khushbu-Kapade

## Source Code Overview

The project follows a modular Python-based structure to ensure clarity, maintainability, and separation of concerns. Each module is responsible for a specific aspect of the system.

The project is implemented entirely in Python and follows a modular design:

- **User Interface:** Streamlit-based web interface for interacting with public health data, generating records, viewing statistics, and visualising trends.
- **Data Management Layer:** SQLite-based persistence layer for storing, updating, and deleting public health records.
- **Data Generation Module:** Synthetic data generation logic used to create realistic public health records without relying on external APIs or CSV datasets.
- **Analytics Module:** Summary statistics and trend analysis for key public health metrics.
- **Testing:** Test-Driven Development (TDD) approach using PyTest to validate data generation, database operations, and analytical functionality.
