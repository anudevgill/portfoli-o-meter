from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def get_sample_data():
    data_array = []
    results_array = []

    with open('good_portfolios.txt', 'r') as good_data:
        for line in good_data:
            data_array.append(line)
            results_array.append(1)

    with open('bad_portfolios.txt', 'r') as bad_data:
        for line in bad_data:
            data_array.append(line)
            results_array.append(0)
    
    cv = CountVectorizer()
    vectorized = cv.fit_transform(data_array)

    X_train, X_test, y_train, y_test = train_test_split(vectorized.toarray(), results_array, train_size=0.7)
    return X_train, y_train, X_test, y_test

def train_and_test():
    X_train, y_train, X_test, y_test = get_sample_data()

    highest_acc = -1
    best_criterion = ""
    best_depth = 0

    for i in range(2, 6):
        for criteria in ["entropy", "gini", "log_loss"]:
            clf = DecisionTreeClassifier(criterion=criteria, max_depth=i)
            clf.fit(X_train, y_train)
            acc = accuracy_score(clf.predict(X_test), y_test)

            if acc > highest_acc:
                highest_acc = acc
                best_criterion = criteria
                best_depth = i

    clf = DecisionTreeClassifier(criterion=best_criterion, max_depth=best_depth)
    clf.fit(X_train, y_train)
    acc = accuracy_score(clf.predict(X_test), y_test)
    print(acc)
    return clf

def score_data(clf):
    score = 0
    num_lines = 0

    with open("portfolio.txt", "r") as new_data:
        for line in new_data:
            score += clf.predict(line)
            num_lines += 1
    
    out_of_five = (score / num_lines) * 5
    
    return round(out_of_five, 2)

if __name__ == "__main__":
    train_and_test()