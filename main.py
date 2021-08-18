from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL



app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost 3306'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = 'yes'
app.config['MySQL_DB'] = 'viajes'
mysql = MySQL(app)


@app.route('/')
def form():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM viajes')
    data = cur.fetchall()
    return render_template("/Formulario.html", registros = data )

@app.route('/Agregar', methods=['POST'])
def Agregar():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Inicio = request.form['Inicio']
        Final = request.form['Final']
        Fecha = request.form['Fecha']
        Ruta = request.form['Ruta']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO viajes (Nombre, Inicio, Final, Fecha, Ruta ) VALUES (%s, %s, %s, %s, %s)',
                    (Nombre, Inicio, Final, Fecha, Ruta))
        mysql.connection.commit()
        return redirect(url_for('/Formulario.html'))

@app.route('/Eliminar/<string:id>')
def Eliminar_viaje(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM viajes WHERE id = {0}'.__format__(id))
    mysql.connection.commit()
    return redirect(url_for('/Formulario.html'))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port= 3000, debug= True)