#regression.py

import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def show_regression(df):
    st.write("### Regression")

    # Select target column
    target_col = st.selectbox("Select target column", df.columns)
    
    # Select feature columns
    feature_cols = st.multiselect("Select feature columns", df.columns.difference([target_col]))
    
    if not feature_cols:
        st.warning("Please select feature columns.")
        return
    
    X = df[feature_cols]
    y = df[target_col]

    # Split the data
    test_size = st.slider("Test size", min_value=0.1, max_value=0.5, step=0.1, value=0.3)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Select regressor
    regressor = st.selectbox("Select regressor", ["Linear Regression", "Random Forest", "SVR"])

    if st.button("Train and Evaluate"):
        if regressor == "Linear Regression":
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
        elif regressor == "Random Forest":
            from sklearn.ensemble import RandomForestRegressor
            model = RandomForestRegressor()
        elif regressor == "SVR":
            from sklearn.svm import SVR
            model = SVR()

        # Train the model
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        st.write("### Results")
        st.write(f"Mean Squared Error: {mse}")
        st.write(f"R² Score: {r2}")
