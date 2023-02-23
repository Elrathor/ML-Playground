from sklearn import tree

if __name__ == '__main__':
    inputValues = [
        [0, 0],  # => 0
        [1, 1],  # => 1
        [2, 2],  # => 2
        [3, 3]   # => 3
    ]
    targetValues = [0, 1, 2, 3]
    treeClassifier = tree.DecisionTreeClassifier()
    treeClassifier = treeClassifier.fit(inputValues, targetValues)

    result = treeClassifier.predict([[2.5, 2.5]])

    if result == [2]:
        print("Hello World 😎")
    else:
        print(result)