from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def train_and_rate(filename):
    data_array = []
    results_array = [1] * 100 + [0] * 100
    num_lines = 200

    # getting training data
    with open('training_data.txt', 'r') as sample_data:
        for line in sample_data:
            data_array.append(line)

    # getting new data from user's portfolio        
    with open(filename, 'r') as new_data:
        for line in new_data:
            data_array.append(line)
            results_array.append(0)
            num_lines += 1
    
    # vectorizing data
    cv = CountVectorizer()
    vectorized = cv.fit_transform(data_array)

    # splitting data into training and test
    X_train, X_test, y_train, _ = train_test_split(vectorized.toarray(), results_array, train_size=(200 / num_lines))

    # building decision tree classifier with criterion="entropy" and max_depth=5
    # these paramters were chosen after testing various paramters with test data 
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=5)
    clf.fit(X_train, y_train)
    
    # generate a score out of 5 (rounded to 2 decimal places) for the user's portfolio
    score = clf.predict(X_test)
    return round((sum(score) / len(score)) * 5, 2)

if __name__ == "__main__":
    print(train_and_rate("sampleResume.txt"))