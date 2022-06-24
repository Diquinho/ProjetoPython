from server import app
from flaskext.mysql import MySQL
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dico2310'
app.config['MYSQL_DATABASE_DB'] = 'tbl_animal'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
