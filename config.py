# Configuraciones de Flask y correo
class Config:
    SECRET_KEY = "super_secreta_clave_gimnasio"  # Para sesiones y seguridad
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "fgym97638@gmail.com"          # Correo que recibirá notificaciones
    MAIL_PASSWORD = "Gym12345"                     # Contraseña del correo (solo para este backend)
