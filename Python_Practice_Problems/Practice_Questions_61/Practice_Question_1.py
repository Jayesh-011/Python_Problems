from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,classification_report
                

def main():
    X = [
        [25, 500, 12, 1, 2],
        [30, 700, 24, 0, 1],
        [45, 1200, 6, 5, 8],
        [50, 1500, 5, 6, 10],
        [28, 600, 18, 1, 1],
        [35, 800, 30, 0, 0],
        [48, 1400, 4, 7, 9],
        [52, 1600, 3, 8, 12],
        [27, 550, 20, 0, 1],
        [42, 1300, 8, 4, 7]
         ]
    
    y = [
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
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

    test = scaler.transform([[46,1450,5,6,9]])

    result = model.predict(test)

    print("The result of the test sample is :","Customer may stay" if result == 0 else "Customer may leave")

if __name__ == "__main__":
    main()