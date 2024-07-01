# # app.py
 
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
 
# # Function to load and display data
# def load_data(file):
#     df = pd.read_csv(file)
#     return df
 
# # Function to perform EDA
# def perform_eda(df):
 
#     st.set_option('deprecation.showfileUploaderEncoding', False)
#     st.set_option('deprecation.showPyplotGlobalUse', False)
 
#     # Display basic info about the dataframe
#     st.write('**Data Preview:**')
#     st.write(df.sample(10))
 
#     st.write('**Data Shape:**')
#     st.write(df.shape)
 
#     # Identify numeric and categorical columns
#     numeric_cols = df.select_dtypes(include=['number']).columns
#     categorical_cols = df.select_dtypes(include=['object', 'category']).columns
 
#     # Display the number of numeric and categorical columns
#     st.write(f'**Number of Numeric Columns:** {len(numeric_cols)}')
#     st.write(f'**Numeric Columns:** {", ".join(numeric_cols)}')
 
#     st.write(f'**Number of Categorical Columns:** {len(categorical_cols)}')
#     st.write(f'**Categorical Columns:** {", ".join(categorical_cols)}')
 
#     # Display descriptive statistics
#     st.write('**Descriptive Statistics:**')
#     st.write(df.describe())
 
#     # Display missing values
#     st.write('**Missing Values:**')
#     st.write(df.isnull().sum())
 
#     # Iterate through columns to check if numeric and plot distributions
#     st.write('**Check Columns Distribution:**')
#     # Display numeric columns for selection
#     numeric_cols = df.select_dtypes(include=['number']).columns
#     selected_col = st.selectbox('Select a column for detailed analysis:', numeric_cols)
 
#     if selected_col:
#         st.subheader(f'Column: {selected_col}')
 
#         # Display box plot and KDE plot in the same row
#         fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
 
#         # Box plot
#         sns.boxplot(x=df[selected_col], ax=ax1)
#         ax1.set_title('Box Plot')
 
#         # KDE plot
#         sns.kdeplot(df[selected_col], shade=True, ax=ax2)
#         ax2.set_title('KDE Plot')
 
#         # Display the plots
#         st.pyplot(fig)
 
#     # Analyze categorical columns
#     st.write('**Categorical Column Analysis:**')
#     categorical_cols = df.select_dtypes(include=['object', 'category']).columns
#     selected_cat_col = st.selectbox('Select a categorical column for analysis:', categorical_cols)
 
#     if selected_cat_col:
#         st.subheader(f'Column: {selected_cat_col}')
 
#         # Display count plot for categorical column
#         plt.figure(figsize=(10, 6))
#         sns.countplot(x=selected_cat_col, data=df)
#         plt.title(f'Count Plot of {selected_cat_col}')
#         plt.xticks(rotation=45)
#         st.pyplot()
 
#         # Frequency analysis for categorical column
#         st.write('**Frequency Analysis:**')
#         freq_table = df[selected_cat_col].value_counts().reset_index()
#         freq_table.columns = [selected_cat_col, 'Frequency']
#         st.write(freq_table)
    
    
#     # Check correlation between two numerical columns
#     st.write('**Correlation Analysis:**')
#     col1, col2 = st.selectbox('Select first column:', numeric_cols), st.selectbox('Select second column:', numeric_cols)

#     if col1 and col2:
#         st.subheader(f'Correlation between {col1} and {col2}')
#         correlation = df[col1].corr(df[col2])
#         st.write(f'Correlation coefficient: {correlation}')

#         # Display scatter plot
#         plt.figure(figsize=(10, 6))
#         sns.scatterplot(x=df[col1], y=df[col2])
#         plt.title(f'Scatter Plot of {col1} vs {col2}')
#         st.pyplot()
 
 
 
 
# # Main function
# def main():
#     st.title('EDA App')
 
#     # File upload and EDA
#     st.sidebar.title('Upload CSV File')
#     uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])
 
#     if uploaded_file is not None:
#         st.sidebar.write('File successfully uploaded!')
#         df = load_data(uploaded_file)
 
#         # Perform EDA
#         perform_eda(df)
 
#     else:
#         st.sidebar.write('Awaiting file to be uploaded.')
        
        

 
# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load and display data
def load_data(file):
    df = pd.read_csv(file)
    return df

# Function to perform EDA
def perform_eda(df):
    st.write('**Data Preview:**')
    st.write(df.sample(10))

    st.write('**Data Shape:**')
    st.write(df.shape)

    # Identify numeric and categorical columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    st.write(f'**Number of Numeric Columns:** {len(numeric_cols)}')
    st.write(f'**Numeric Columns:** {", ".join(numeric_cols)}')

    st.write(f'**Number of Categorical Columns:** {len(categorical_cols)}')
    st.write(f'**Categorical Columns:** {", ".join(categorical_cols)}')

    st.write('**Descriptive Statistics:**')
    st.write(df.describe())

    st.write('**Missing Values:**')
    st.write(df.isnull().sum())

    st.write('**Check Columns Distribution:**')
    selected_col = st.selectbox('Select a column for detailed analysis:', numeric_cols)

    if selected_col:
        st.subheader(f'Column: {selected_col}')

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        sns.boxplot(x=df[selected_col], ax=ax1)
        ax1.set_title('Box Plot')

        sns.kdeplot(df[selected_col], shade=True, ax=ax2)
        ax2.set_title('KDE Plot')

        st.pyplot(fig)

    st.write('**Categorical Column Analysis:**')
    selected_cat_col = st.selectbox('Select a categorical column for analysis:', categorical_cols)

    if selected_cat_col:
        st.subheader(f'Column: {selected_cat_col}')

        plt.figure(figsize=(10, 6))
        sns.countplot(x=selected_cat_col, data=df)
        plt.title(f'Count Plot of {selected_cat_col}')
        plt.xticks(rotation=45)
        st.pyplot()

        st.write('**Frequency Analysis:**')
        freq_table = df[selected_cat_col].value_counts().reset_index()
        freq_table.columns = [selected_cat_col, 'Frequency']
        st.write(freq_table)

    st.write('**Correlation Analysis:**')
    col1, col2 = st.selectbox('Select first column:', numeric_cols), st.selectbox('Select second column:', numeric_cols)

    if col1 and col2:
        st.subheader(f'Correlation between {col1} and {col2}')
        correlation = df[col1].corr(df[col2])
        st.write(f'Correlation coefficient: {correlation}')

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=df[col1], y=df[col2])
        plt.title(f'Scatter Plot of {col1} vs {col2}')
        st.pyplot()

# Function to perform preprocessing
def perform_preprocessing(df):
    st.write('**Preprocessing Section**')
    
    # Fill missing values
    st.write('**Fill Missing Values**')

    # Numeric columns
    st.write('**Numerical Columns**')
    numeric_cols = df.select_dtypes(include=['number']).columns
    num_fill_method = st.selectbox('Select a method to fill missing values in numerical columns:',
                                   ['Mean', 'Median', 'Forward Fill', 'Backward Fill', 'Custom Value'])
    if num_fill_method == 'Mean':
        df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.mean()))
        st.write('Missing values filled with mean.')
    elif num_fill_method == 'Median':
        df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.median()))
        st.write('Missing values filled with median.')
    elif num_fill_method == 'Forward Fill':
        df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(method='ffill'))
        st.write('Missing values filled with forward fill.')
    elif num_fill_method == 'Backward Fill':
        df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(method='bfill'))
        st.write('Missing values filled with backward fill.')
    elif num_fill_method == 'Custom Value':
        custom_value = st.number_input('Enter a custom value to fill missing values:', value=0)
        df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(custom_value))
        st.write(f'Missing values filled with custom value: {custom_value}')

    # Categorical columns
    st.write('**Categorical Columns**')
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    cat_fill_method = st.selectbox('Select a method to fill missing values in categorical columns:',
                                   ['Mode', 'Forward Fill', 'Backward Fill', 'Custom Value'])
    if cat_fill_method == 'Mode':
        df[categorical_cols] = df[categorical_cols].apply(lambda col: col.fillna(col.mode()[0]))
        st.write('Missing values filled with mode.')
    elif cat_fill_method == 'Forward Fill':
        df[categorical_cols] = df[categorical_cols].apply(lambda col: col.fillna(method='ffill'))
        st.write('Missing values filled with forward fill.')
    elif cat_fill_method == 'Backward Fill':
        df[categorical_cols] = df[categorical_cols].apply(lambda col: col.fillna(method='bfill'))
        st.write('Missing values filled with backward fill.')
    elif cat_fill_method == 'Custom Value':
        custom_value = st.text_input('Enter a custom value to fill missing values:', value='')
        df[categorical_cols] = df[categorical_cols].apply(lambda col: col.fillna(custom_value))
        st.write(f'Missing values filled with custom value: {custom_value}')

    st.write('**Drop Duplicates**')
    if st.button('Drop Duplicates'):
        df.drop_duplicates(inplace=True)
        st.write('Duplicates dropped.')

    st.write('**Remove Columns**')
    columns_to_remove = st.multiselect('Select columns to remove:', df.columns)
    if st.button('Remove Selected Columns'):
        df.drop(columns=columns_to_remove, inplace=True)
        st.write(f'Removed columns: {columns_to_remove}')

    st.write('**Preprocessed Data Preview**')
    st.write(df.head())

    st.write('**Download Preprocessed Data**')
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label='Download CSV',
        data=csv,
        file_name='preprocessed_data.csv',
        mime='text/csv',
    )

# Main function
def main():
    st.title('Exploratory data analysis (EDA) and Preprocessing WebApp')

    # File upload
    st.sidebar.title('Upload CSV File')
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.sidebar.write('File successfully uploaded!')

        # Menu
        st.sidebar.title('Menu')
        option = st.sidebar.radio('Select an option:', ['EDA', 'Preprocessing'])

        if option == 'EDA':
            perform_eda(df)
        elif option == 'Preprocessing':
            perform_preprocessing(df)

    else:
        st.sidebar.write('Awaiting file to be uploaded.')

if __name__ == "__main__":
    main()
