from flask import Flask, redirect, url_for, render_template, request, flash
from datetime import datetime
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = 'flask_secret_key' #should change for real key

# connect to DB
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flaskproject'

mysql = MySQL(app)

# context processor
@app.context_processor
def date_now():
  return {
    'now': datetime.utcnow()
  }

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/info')
@app.route('/info/<string:name>')
def info(name=None):
  return render_template('info.html', name=name)

@app.route('/contact-us')
@app.route('/contact-us/<redirection>')
def contact(redirection=None):
  if redirection is not None:
    return redirect(url_for('index'))
    
  return render_template('contact.html')


@app.route('/create-car', methods=['GET', 'POST'])
def create_car():
  if request.method == 'POST':

    brand = request.form['brand']
    model = request.form['model']
    price = request.form['price']
    city = request.form['city']

    cursor = mysql.get_db().cursor()
    cursor.execute("INSERT INTO autos VALUES(NULL, %s, %s, %s, %s)", (brand, model, price, city))
    cursor.connection.commit()
    cursor.close()

    flash('Auto creado')
    return redirect(url_for('index'))

  return render_template('create_car.html')

@app.route('/cars')
def cars():
  cursor = mysql.get_db().cursor()
  cursor.execute("SELECT * FROM autos")
  cars = cursor.fetchall()
  cursor.close()

  return render_template('cars.html', cars=cars)

@app.route('/car/<id>')
def car(id):
  cursor = mysql.get_db().cursor()
  cursor.execute("SELECT * FROM autos WHERE id = %s", (id))
  car = cursor.fetchall()
  cursor.close()

  return render_template('car.html', car=car[0])

@app.route('/delete-car/<id>')
def delete_car(id):
  cursor = mysql.get_db().cursor()
  cursor.execute("DELETE FROM autos WHERE id = %s", (id))
  cursor.connection.commit()
  cursor.close()

  flash('Auto eliminado')
  return redirect(url_for('cars'))

@app.route('/edit-car/<id>', methods=['GET', 'POST'])
def edit_car(id):
  if request.method == 'POST':

    brand = request.form['brand']
    model = request.form['model']
    price = request.form['price']
    city = request.form['city']

    cursor = mysql.get_db().cursor()
    cursor.execute(
      """
      UPDATE autos 
      SET brand=%s, model=%s, price=%s, city=%s
      WHERE id = %s
      """,
      (brand, model, price, city, id)
    )
    cursor.connection.commit()
    cursor.close()

    flash('Auto guardado')
    return redirect(url_for('cars'))

  cursor = mysql.get_db().cursor()
  cursor.execute("SELECT * FROM autos WHERE id = %s", (id))
  car = cursor.fetchall()
  cursor.close()
  return render_template('create_car.html', car=car[0])


if __name__ == '__main__':
  app.run(debug=True)