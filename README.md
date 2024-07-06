
# EDA & Preprocessing Web App

This Streamlit application allows users to upload a CSV file, perform exploratory data analysis (EDA), preprocess the data, and apply machine learning algorithms for classification and regression tasks.

## Live Demo

Check out the live demo of the app [here](https://eda-web-app-t9mt.onrender.com/).

## Features

### Upload CSV File
- **File Upload**: Upload a CSV file directly from your local machine.
- **File Size Limit**: Supports files up to 200MB.

### Exploratory Data Analysis (EDA)
- **Data Preview**: View the uploaded data.
- **Data Shape**: Display the shape of the data.
- **Descriptive Statistics**: Summary statistics for numerical columns.
- **Missing Values Summary**: Identify missing values in the dataset.
- **Column Distribution Analysis**: Visualize the distribution of values in numerical columns using box plots and KDE plots.
- **Categorical Column Analysis**: Frequency analysis and count plots for categorical columns.
- **Correlation Analysis**: Scatter plots and correlation coefficients for pairs of numerical columns.
- **Correlation Heatmap**: Visualize the correlation matrix of numerical columns.

### Preprocessing
- **Fill Missing Values**:
  - Numerical Columns: Fill with mean, median, forward fill, backward fill, or a custom value.
  - Categorical Columns: Fill with mode, forward fill, backward fill, or a custom value.
- **Drop Duplicates**: Remove duplicate rows from the dataset.
- **Remove Columns**: Drop selected columns from the dataset.
- **Scale Numerical Data**: Scale numerical columns using Standard Scaler or Min-Max Scaler.
- **Encode Categorical Data**: Encode categorical columns using Label Encoding or One-Hot Encoding.
- **Preview Preprocessed Data**: View the preprocessed dataset.
- **Download Preprocessed Data**: Download the preprocessed data as a CSV file.

### Machine Learning Algorithms
- **Classification**:
  - Select target and feature columns.
  - Split data into training and testing sets.
  - Choose between Logistic Regression, Random Forest, and SVM classifiers.
  - Train the model and evaluate performance using accuracy and classification report.
- **Regression**:
  - Select target and feature columns.
  - Split data into training and testing sets.
  - Choose between Linear Regression, Random Forest, and SVR regressors.
  - Train the model and evaluate performance using mean squared error and R² score.

## How to Run the App Locally

1. **Clone this repository**:
   ```sh
   git clone https://github.com/monish0001/EDA_Web_App.git
   cd EDA_Web_App
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```sh
   streamlit run app.py
   ```

## Dependencies

The app requires the following Python libraries:
- streamlit
- pandas
- matplotlib
- seaborn
- scikit-learn

You can install these libraries using the command:
```sh
pip install streamlit pandas matplotlib seaborn scikit-learn
```

## Usage

1. Open the app in your browser.
2. Upload a CSV file using the file uploader on the main page.
3. Choose "EDA", "Preprocessing", or "ML Algorithms" from the menu in the left sidebar.
4. Follow the instructions in the selected section to perform EDA, preprocessing, or apply machine learning algorithms.
5. Download the preprocessed data as a CSV file (available in the Preprocessing section).

## Contributing

Contributions are welcome! If you have any suggestions or find any bugs, please open an issue or create a pull request.

## Acknowledgements

- **Streamlit** for providing an easy-to-use framework for building web apps.
- **Pandas** for data manipulation and analysis.
- **Matplotlib** and **Seaborn** for data visualization.
- **Scikit-learn** for machine learning algorithms.

## License

This software is provided for educational purposes only. Anyone is free to use this software for learning and educational purposes.


## Contact

For any questions or suggestions, please contact mohdmonishksg@gmail.com.
