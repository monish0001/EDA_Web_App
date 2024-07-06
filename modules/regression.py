import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_squared_log_error

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
    regressor = st.selectbox("Select regressor", [
        "Linear Regression",
        "Logistic Regression",
        "Polynomial Regression",
        "Support Vector Regression",
        "Decision Tree Regression",
        "Random Forest Regression",
        "Ridge Regression",
        "Lasso Regression"
    ])

    # Get hyperparameters
    params = {}
    if regressor == "Logistic Regression":
        params['max_iter'] = st.number_input("Max Iterations", value=100)
        params['C'] = st.number_input("Regularization strength (C)", value=1.0)
    elif regressor == "Polynomial Regression":
        params['degree'] = st.number_input("Degree of the polynomial features", value=2)
    elif regressor == "Support Vector Regression":
        params['C'] = st.number_input("Regularization parameter (C)", value=1.0)
        params['epsilon'] = st.number_input("Epsilon in the epsilon-SVR model", value=0.1)
    elif regressor == "Decision Tree Regression":
        params['max_depth'] = st.number_input("Max Depth", value=5)
    elif regressor == "Random Forest Regression":
        params['n_estimators'] = st.number_input("Number of Trees", value=100)
        params['max_depth'] = st.number_input("Max Depth", value=5)
    elif regressor == "Ridge Regression":
        params['alpha'] = st.number_input("Regularization strength (alpha)", value=1.0)
    elif regressor == "Lasso Regression":
        params['alpha'] = st.number_input("Regularization strength (alpha)", value=1.0)

    if st.button("Train and Evaluate"):
        if regressor == "Linear Regression":
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
        elif regressor == "Logistic Regression":
            from sklearn.linear_model import LogisticRegression
            model = LogisticRegression(**params)
        elif regressor == "Polynomial Regression":
            from sklearn.preprocessing import PolynomialFeatures
            from sklearn.linear_model import LinearRegression
            poly_features = PolynomialFeatures(degree=params['degree'])
            X_train = poly_features.fit_transform(X_train)
            X_test = poly_features.transform(X_test)
            model = LinearRegression()
        elif regressor == "Support Vector Regression":
            from sklearn.svm import SVR
            model = SVR(**params)
        elif regressor == "Decision Tree Regression":
            from sklearn.tree import DecisionTreeRegressor
            model = DecisionTreeRegressor(**params)
        elif regressor == "Random Forest Regression":
            from sklearn.ensemble import RandomForestRegressor
            model = RandomForestRegressor(**params)
        elif regressor == "Ridge Regression":
            from sklearn.linear_model import Ridge
            model = Ridge(**params)
        elif regressor == "Lasso Regression":
            from sklearn.linear_model import Lasso
            model = Lasso(**params)

        # Train the model
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        msle = mean_squared_log_error(y_test, y_pred)

        st.write("### Results")
        st.write(f"Mean Squared Error (MSE): {mse}")
        st.write(f"Mean Absolute Error (MAE): {mae}")
        st.write(f"Mean Squared Log Error (MSLE): {msle}")
        st.write(f"R² Score: {r2}")

