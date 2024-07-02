import streamlit as st
from streamlit import session_state
from modules.data_loader import load_data
from modules.eda import show_eda
from modules.preprocessing import show_preprocessing, fill_missing_values

def main():
    st.title('Exploratory Data Analysis (EDA) and Preprocessing WebApp')

    # Initialize session_state variables
    if 'df' not in session_state:
        session_state.df = None
    if 'file_uploaded' not in session_state:
        session_state.file_uploaded = False

    st.sidebar.title('Upload CSV File')
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if not session_state.file_uploaded:
            st.sidebar.success('File successfully uploaded!')
            session_state.file_uploaded = True
        
        # Store the dataframe in session_state
        session_state.df = df
        
        st.sidebar.title('Menu')
        option = st.sidebar.radio('Select an option:', ['Preprocessing', 'EDA'])

        if option == 'EDA':
            show_eda(session_state.df)
        elif option == 'Preprocessing':
            show_preprocessing(session_state.df)
    else:
        if not session_state.file_uploaded:
            st.sidebar.info('Awaiting file to be uploaded.')

if __name__ == "__main__":
    main()
