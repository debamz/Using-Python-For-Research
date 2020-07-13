This code fills in the function correctly:

def accuracy(predictions, outcomes):
    return 100*np.mean(predictions == outcomes)

print(accuracy(x,y))
51.5
