from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffe = IntegerField('Coffe', validators=[NumberRange(min=0, max=5, message="Min of 1 and Max 5"), DataRequired()])
    wifi = IntegerField('Wifi', validators=[NumberRange(min=0, max=5, message="Min of 1 and Max 5"), DataRequired()])
    power = IntegerField('Power', validators=[NumberRange(min=0, max=5, message="Min of 1 and Max 5"), DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    coffe = "☕" * int(form.coffe.data)
    wifi = "💪" * int(form.wifi.data)
    power = "🔌" * int(form.power.data)
    print(int(form.coffe.data))
    dados = [
        {
            'Cafe name': form.cafe.data,
            'Location': form.location.data,
            'Open': form.open.data,
            'Close': form.close.data,
            'Coffe': coffe,
            'Wifi': wifi,
            'Power': power
        }
    ]
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=dados[0].keys())
            for dado in dados:
                writer.writerow(dado)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
