#TODO:configurar la constraseña acorde a el equipo, seguido de "root:"
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost/flask_shopy_2687386"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Delusion'
#localhost/flask_shopy_2687386