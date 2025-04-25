# Movie Rating Prediction

## Overview
This project is focused on building a predictive model to estimate movie ratings based on attributes like genre, director, actors, duration, and more. The dataset used is from IMDb (Indian Movies).

### Features:
- Data Preprocessing (handling missing values, encoding categorical variables)
- Feature Engineering (e.g., director's average rating, movie age)
- Predictive Model (Random Forest Regressor)

## Project Structure
- **data/**: Contains the dataset (e.g., `IMDb_Movies.csv`)
- **notebooks/**: Jupyter notebooks with code for data preprocessing, model building, and evaluation
- **scripts/**: Python scripts with helper functions
- **requirements.txt**: List of libraries required for the project
- **README.md**: This file

## Dependencies
This project requires the following libraries:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

You can install them using:
pip install -r requirements.txt

## Running the Project
1. Download the dataset (available [here](https://www.kaggle.com/datasets/adrianmcmahon/imdb-india-movies)).
2. Load the dataset using the Jupyter notebook or Google Collab `movie_rating_model.ipynb`.
3. Follow the steps in the notebook to preprocess the data, build the model, and evaluate performance.

## Evaluation Metrics
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R2 Score
