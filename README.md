# Super Market Item Sales Predictor

This is a Streamlit application that predicts the sales of super market items based on various features. It uses a machine learning model trained on 
historical sales data to make predictions.

## Usage

1. Open your web browser and navigate to https://supermarket-sales-predictor.streamlit.app/

2. Fill in the input fields with the relevant information for the item.

3. Click the "Predict" button to get the predicted sales for the item.

## Features

- Item Weight: Enter the weight of the item.
- Item Fat Content: Select the fat content of the item from the available options.
- Item Visibility: Enter the visibility of the item.
- Item Type: Select the type of the item from the available options.
- MRP: Enter the Maximum Retail Price (MRP) of the item.
- Years of Operation: Enter the number of years the outlet has been in operation.
- Outlet Size: Select the size of the outlet from the available options.
- Outlet Location Type: Select the location type of the outlet from the available options.
- Outlet Types: Select the type of the outlet from the available options.

## Prediction

Once you have filled in all the necessary information, click the "Predict" button. The application will use a pre-trained machine learning model to predict the sales of the item. The predicted sales value will be displayed on the screen.

## File Descriptions

- `app.py`: The main Streamlit application file.
- `styles.css`: CSS file for custom styling of the application.
- `prediction_model`: Pre-trained machine learning model for sales prediction.
- `requirements.txt`: List of required Python packages.
- `Sales Prediction Model.ipynb`:Jupyter Notebook file containing the code for training and evaluating the sales prediction model.
