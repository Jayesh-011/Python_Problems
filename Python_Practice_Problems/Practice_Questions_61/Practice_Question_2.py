from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,classification_report
                

def main():
    X = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
    ]
    
    y = [
    0, 1, 1, 0, 1,
    1, 0, 1, 0, 1
    ]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.2,random_state=42)

    model = MLPClassifier(
        hidden_layer_sizes=(10,),
        activation="relu",
        learning_rate="adaptive",
        solver="lbfgs",
        random_state=42,
        max_iter=300
    )

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    print("Accuracy of the model is :",accuracy_score(y_test,y_pred))

    print("Classification Report :\n",classification_report(y_test,y_pred))

    test = scaler.transform([[55000, 720, 400000, 10000, 1]])

    result = model.predict(test)

    print("The result of the test sample is :","Loan rejected" if result == 0 else "Loan approved")

if __name__ == "__main__":
    main()