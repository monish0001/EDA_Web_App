import streamlit as st
from streamlit import session_state

def show_preprocessing(df):
    st.write('**Preprocessing Section**')
    
    # Ensure data persistence
    if 'df' not in session_state:
        session_state.df = df
    else:
        session_state.df = df
    
    fill_missing_values()
    drop_duplicates()
    remove_columns()
    preview_preprocessed_data()
    download_preprocessed_data()
    show_missing_data()

def show_missing_data():
    df = session_state.df 
    st.write('**Missing Values:**')
    st.write(df.isnull().sum())

def fill_missing_values():
    df = session_state.df  # Retrieve DataFrame from session_state
    st.write('**Fill Missing Values**')

    # Filter numeric and categorical columns with missing values
    numeric_cols_with_nulls = [col for col in df.select_dtypes(include=['number']).columns if df[col].isnull().sum() > 0]
    categorical_cols_with_nulls = [col for col in df.select_dtypes(include=['object', 'category']).columns if df[col].isnull().sum() > 0]

    if not numeric_cols_with_nulls and not categorical_cols_with_nulls:
        st.write('No missing values found in any columns.')
        return

    # Dictionary to store fill methods
    fill_methods = {}

    # For Numerical Columns
    if numeric_cols_with_nulls:
        st.write('**Numerical Columns**')
        for col in numeric_cols_with_nulls:
            st.write(f'Column: {col}')
            fill_method = st.selectbox(f'Select method to fill missing values in {col}:',
                                       ['Mean', 'Median', 'Forward Fill', 'Backward Fill', 'Custom Value'], key=f'num_method_{col}')
            fill_methods[col] = fill_method
            if fill_method == 'Custom Value':
                fill_methods[col] = (fill_method, st.number_input(f'Enter a custom value for {col}:', key=f'custom_num_value_{col}'))

    # For Categorical Columns
    if categorical_cols_with_nulls:
        st.write('**Categorical Columns**')
        for col in categorical_cols_with_nulls:
            st.write(f'Column: {col}')
            fill_method = st.selectbox(f'Select method to fill missing values in {col}:',
                                       ['Mode', 'Forward Fill', 'Backward Fill', 'Custom Value'], key=f'cat_method_{col}')
            fill_methods[col] = fill_method
            if fill_method == 'Custom Value':
                fill_methods[col] = (fill_method, st.text_input(f'Enter a custom value for {col}:', key=f'custom_cat_value_{col}'))

    if st.button('Fill Missing Values'):
        for col, method in fill_methods.items():
            if isinstance(method, tuple):  # Custom Value
                method, custom_value = method
                df[col].fillna(custom_value, inplace=True)
            elif method == 'Mean':
                df[col].fillna(df[col].mean(), inplace=True)
            elif method == 'Median':
                df[col].fillna(df[col].median(), inplace=True)
            elif method == 'Forward Fill':
                df[col].fillna(method='ffill', inplace=True)
            elif method == 'Backward Fill':
                df[col].fillna(method='bfill', inplace=True)
            elif method == 'Mode':
                df[col].fillna(df[col].mode()[0], inplace=True)
        
        st.write('Missing values have been filled.')

    # Update session_state with modified DataFrame
    session_state.df = df

def drop_duplicates():
    df = session_state.df  # Retrieve DataFrame from session_state
    st.write('**Drop Duplicates**')
    if st.button('Drop Duplicates'):
        df.drop_duplicates(inplace=True)
        st.write('Duplicates dropped.')

    # Update session_state with modified DataFrame
    session_state.df = df

def remove_columns():
    df = session_state.df  # Retrieve DataFrame from session_state
    st.write('**Remove Columns**')
    columns_to_remove = st.multiselect('Select columns to remove:', df.columns)
    if st.button('Remove Selected Columns'):
        df.drop(columns=columns_to_remove, inplace=True)
        st.write(f'Removed columns: {columns_to_remove}')

    # Update session_state with modified DataFrame
    session_state.df = df

def preview_preprocessed_data():
    df = session_state.df  # Retrieve DataFrame from session_state
    st.write('**Preprocessed Data Preview**')
    st.write(df.head())

def download_preprocessed_data():
    df = session_state.df  # Retrieve DataFrame from session_state
    st.write('**Download Preprocessed Data**')
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label='Download CSV',
        data=csv,
        file_name='preprocessed_data.csv',
        mime='text/csv',
    )
