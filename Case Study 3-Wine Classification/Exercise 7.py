The following code will give the accuracy:

library_predictions = knn.predict(numeric_data)
print(accuracy(library_predictions, data["high_quality"]))
