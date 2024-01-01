from flask import Flask , render_template , url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pickle

print("test")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST','GET'])
def predict():
    load_model = pickle.load(open('tv_marketing_model.pkl','rb'))
    result = load_model.predict([[float(request.form['Budget'])]])
    return str(result)
    #return request.form['Budget']

if __name__ == "__main__":
    app.run(debug=True)