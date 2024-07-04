import streamlit as st

def show_preprocessing():
    st.write('**Preprocessing Section**')
    
    df = st.session_state.df
    
    if df is None:
        st.write('Please upload data to begin preprocessing.')
        return
    # st.markdown('<hr>', unsafe_allow_html=True)
    # show_missing_data(df)
    st.markdown('<hr>', unsafe_allow_html=True)
    fill_missing_values(df)
    st.markdown('<hr>', unsafe_allow_html=True)
    drop_duplicates(df)
    st.markdown('<hr>', unsafe_allow_html=True)
    remove_columns(df)
    st.markdown('<hr>', unsafe_allow_html=True)
    preview_preprocessed_data(df)
    st.markdown('<hr>', unsafe_allow_html=True)
    download_preprocessed_data(df)
    st.markdown('<hr>', unsafe_allow_html=True)
    
    
def show_missing_data(df):
    st.write('**Missing Values:**')
    st.write(df.isnull().sum())
    st.write(f'Total Missing Values : {df.isnull().sum().sum()}')
    
    
def fill_missing_values(df):
    st.write('**Fill Missing Values**')

    numeric_cols_with_nulls = [col for col in df.select_dtypes(include=['number']).columns if df[col].isnull().sum() > 0]
    categorical_cols_with_nulls = [col for col in df.select_dtypes(include=['object', 'category']).columns if df[col].isnull().sum() > 0]

    if not numeric_cols_with_nulls and not categorical_cols_with_nulls:
        st.write('No missing values found in any columns.')
        return

    fill_methods = {}

    if numeric_cols_with_nulls:
        st.write('**Numerical Columns**')
        for col in numeric_cols_with_nulls:
            fill_method = st.selectbox(f'Select method to fill missing values in {col}:',
                                       ['Mean', 'Median', 'Forward Fill', 'Backward Fill', 'Custom Value'], key=f'num_method_{col}')
            fill_methods[col] = fill_method
            if fill_method == 'Custom Value':
                fill_methods[col] = (fill_method, st.number_input(f'Enter a custom value for {col}:', key=f'custom_num_value_{col}'))

    if categorical_cols_with_nulls:
        st.write('**Categorical Columns**')
        for col in categorical_cols_with_nulls:
            fill_method = st.selectbox(f'Select method to fill missing values in {col}:',
                                       ['Mode', 'Forward Fill', 'Backward Fill', 'Custom Value'], key=f'cat_method_{col}')
            fill_methods[col] = fill_method
            if fill_method == 'Custom Value':
                fill_methods[col] = (fill_method, st.text_input(f'Enter a custom value for {col}:', key=f'custom_cat_value_{col}'))

    if st.button('Fill Missing Values'):
        for col, method in fill_methods.items():
            if isinstance(method, tuple):
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

    st.session_state.df = df

def drop_duplicates(df):
    st.write('**Drop Duplicates**')
    if st.button('Drop Duplicates'):
        df.drop_duplicates(inplace=True)
        st.write('Duplicates dropped.')

    st.session_state.df = df

def remove_columns(df):
    st.write('**Remove Columns**')
    columns_to_remove = st.multiselect('Select columns to remove:', df.columns)
    if st.button('Remove Selected Columns'):
        df.drop(columns=columns_to_remove, inplace=True)
        st.write(f'Removed columns: {columns_to_remove}')

    st.session_state.df = df

def preview_preprocessed_data(df):
    st.write('**Preprocessed Data Preview**')
    st.write(st.session_state.df)

def download_preprocessed_data(df):
    st.write('**Download Preprocessed Data**')
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label='Download CSV',
        data=csv,
        file_name='preprocessed_data.csv',
        mime='text/csv',
    )
