# pipeline = Pipeline([
#     ('preprocessor', preprocessor),
#     ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
# ])

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print('fitting')
# pipeline.fit(X_train, y_train)

# print('predicting')
# y_pred = pipeline.predict(X_test)

# print("Predictions vs Actual:")
# for i, (pred, actual) in enumerate(zip(y_pred, y_test)):
#     print(f"Sample {i+1}: Predicted = ${pred:.0f}, Actual = ${actual}")