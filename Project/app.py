from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

#initializing flask
app = Flask(__name__)
model = pickle.load(open('flight_rf.pkl', 'rb'))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        airline=request.form['airline']
        if(airline=='SpiceJet'):
            airline = 0.08341387594622485
        elif(airline=='AirAsia'):
            airline = 0.0
        elif(airline=='Vistara'):
            airline = 1.0
        elif(airline=='GO_FIRST'):
            airline = 0.062351902783173624
        elif(airline=='Indigo'):
            airline = 0.04925820402105957
        elif (airline=='Air_India'):
            airline = 0.7740141110489556
            
        Source = request.form["source"]
        if (Source == 'Delhi'):
            Source = 0.0
        elif (Source == 'Mumbai'):
            Source = 0.8973113723937232
        elif (Source == 'Bangalore'):
            Source = 0.9649029601678816
        elif (Source == 'Kolkata'):
            Source = 0.8645900039237517
        elif (Source == 'Hyderabad'):
            Source = 0.45096139181338124
        elif (Source == 'Chennai'):
            Source = 1.0

        Destination = request.form["destination"]
        if (Destination == 'Delhi'):
            Destination = 0.0
        elif (Destination == 'Mumbai'):
            Destination = 0.7297646187451479
        elif (Destination == 'Bangalore'):
            Destination = 0.8927552619350294
        elif (Destination == 'Kolkata'):
            Destination = 0.926072273948229
        elif (Destination == 'Hyderabad'):
            Destination = 0.5438347682734648
        elif (Destination == 'Chennai'):
            Destination = 1.0
            
        Departure_Time=request.form["departure"]
        if (Departure_Time == 'Evening'):
            Departure_Time= 0.844886445216259
        elif (Departure_Time == 'Early_Morning'):
            Departure_Time = 0.8002235675226788
        elif (Departure_Time == 'Morning'):
            Departure_Time = 0.8627303864916867
        elif (Departure_Time == 'Afternoon'):
            Departure_Time = 0.634326717283298
        elif (Departure_Time == 'Night'):
            Departure_Time = 1.0
            
        Stops=request.form["stops"]
        if (Stops == 'zero'):
            Stops =  0.0
        elif(Stops == 'one'):
            Stops = 0.9999999999999999
        elif(Stops == 'two_or_more'):
            Stops = 0.2544431773778614
        
        Arrival_Time=request.form["arrival"]
        if (Arrival_Time == 'Night'):
            Arrival_Time = 0.8494714031093153
        elif(Arrival_Time == 'Morning'):
            Arrival_Time = 0.9305030063929658
        elif(Arrival_Time == 'Early_Morning'):
            Arrival_Time = 0.31233769744946915
        elif(Arrival_Time == 'Afternoon'):
            Arrival_Time = 0.6338274648461384
        elif(Arrival_Time == 'Evening'):
            Arrival_Time = 1.0
        
        Class=request.form["class"]
        if(Class =='Economy'):
            Class = 0.0
        elif(Class =='Business'):
            Class = 1.0
            
        Duration=request.form["duration"]
        Days_left=request.form["days_left"]
        
        prediction=model.predict([[
            airline,
            Source,
            Departure_Time,
            Stops,
            Arrival_Time,      
            Destination, 
            Class,
            Duration,
            Days_left
        ]])

        output=round(prediction[0],2)
        

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, jsonify, request, render_template
# import pickle
# import pandas as pd
# app = Flask(__name__)
# model = pickle.load(open('flight_rf.pkl', 'rb'))

# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     source = request.form["source"]
#     destination = request.form['destination']
#     airline = request.form['airline']
#     departure = request.form['departure']
#     arrival = request.form['arrival']
#     duration = float(request.form['duration'])
#     stops = int(request.form['stops'])
#     flight_class = request.form['class']
#     data = {'source': [source],
#             'destination': [destination],
#             'airline': [airline],
#             'departure': [departure],
#             'arrival': [arrival],
#             'duration': [duration],
#             'stops': [stops],
#             'class': [flight_class]}
#     df = pd.DataFrame(data)
#     predictions = model.predict(df)
#     return jsonify({'predictions': predictions.tolist()})

# if __name__ == '__main__':
#     app.run(debug=True)

