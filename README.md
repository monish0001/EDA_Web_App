# EDA and Preprocessing Web App

This Streamlit app allows users to upload a CSV file, perform exploratory data analysis (EDA), and preprocess the data. Users can fill missing values, drop duplicates, and remove selected columns. At the end of the preprocessing, users can download the preprocessed data as a CSV file.

## Live Demo

Check out the live demo of the app [here](https://eda-web-app-t9mt.onrender.com/).

## Features

- **Upload CSV File**: Upload a CSV file from your local machine.
- **Exploratory Data Analysis (EDA)**:
  - Data preview and shape
  - Descriptive statistics
  - Missing values summary
  - Distribution analysis for numerical columns (Box Plot and KDE Plot)
  - Frequency analysis for categorical columns (Count Plot and Frequency Table)
  - Correlation analysis between two numerical columns (Scatter Plot and Correlation Coefficient)
- **Preprocessing**:
  - Fill missing values in numerical columns with mean, median, forward fill, backward fill, or a custom value
  - Fill missing values in categorical columns with mode, forward fill, backward fill, or a custom value
  - Drop duplicate rows
  - Remove selected columns
  - Preview preprocessed data
  - Download preprocessed data as a CSV file

## How to Run the App Locally

1. Clone this repository:
   ```sh
   git clone https://github.com/monish0001/EDA_Web_App.git
   cd EDA_Web_App
   pip install -r requirements.txt
   streamlit run app.py
2. Dependencies
   The app requires the following Python libraries:

  streamlit
  pandas
  matplotlib
  seaborn
  You can install these libraries using the command:
  pip install streamlit pandas matplotlib seaborn

3. Usage
  Open the app in your browser.
  Upload a CSV file using the file uploader on the left sidebar.
  Choose either "EDA" or "Preprocessing" from the menu in the left sidebar.
  Follow the instructions on the selected section to perform EDA or preprocessing.
  Download the preprocessed data as a CSV file (available in the Preprocessing section).

4. Contributing
  Contributions are welcome! If you have any suggestions or find any bugs, please open an issue or create a pull request.


5. Acknowledgements
  Streamlit for providing an easy-to-use framework for building web apps.
  Pandas for data manipulation and analysis.
  Matplotlib and Seaborn for data visualization.
Enjoy exploring and preprocessing your data with this app!
