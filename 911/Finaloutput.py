from flask import Flask, request
import pickle


file = open('./Finalpkl.pkl', 'rb')
model = pickle.load(file)
file.close()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return """
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
       
        <h2>APPLICATION FOR ZipCode PREDICTION</h2>
        <form method="POST" action="/predict">
            Priority <input name="priority" type="text" >
            <button>Predict</button>
           District <input name="district" type="text" >
            <button>Predict</button>
            PoliceDistrict <input name="policeDistrict" type="text" >
            <button>Predict</button>
            
            
           
        </form>
    """

@app.route("/predict", methods=["POST"])
def predict_salary():
    Priority = int(request.form.get("priority"))
    print(f"experience = {Priority}, type = {type(Priority)}")

    District = int(request.form.get("district"))
    print(f"experience = {District}, type = {type(District)}")

    policeDistrict = int(request.form.get("policeDistrict"))
    print(f"experience = {policeDistrict}, type = {type(policeDistrict)}")

    zipcode = model.predict([[Priority, District, policeDistrict]])
    Priority = int(request.form.get("priority"))
    print(zipcode)

    return f"""
    <h1>Prediction of Area</h1>
    <h3>For Priority {Priority} 
        in District No {District} 
        of Police_District No {policeDistrict} 
        Need to visit zipcode --> {zipcode[0]}</h3>
"""

app.run(port=2100)