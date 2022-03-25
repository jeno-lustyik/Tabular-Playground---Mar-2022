import joblib
model_joblib = joblib.load('model.pkl')


while True:

    x = str(input('which cordinate? (0,1,2) \n'))
    y = str(input('which coordinate? (0,1,2,3) \n'))
    d = str(input('which direction? (EB, SB, NB, WB, NE, SE, NW, SW)\n'))
    route = str(x+y+d)

    x_test = [[route]]

    prediction = model_joblib.predict(x_test)

    print(prediction)
