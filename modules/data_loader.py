import pandas as pd
from streamlit import session_state

def load_data(file):
    df = pd.read_csv(file)
    
    # Store the dataframe in session_state
    session_state.df = df
    
    return df
