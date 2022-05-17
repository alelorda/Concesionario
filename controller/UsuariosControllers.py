from asyncio.windows_events import NULL
from data.Usuarios import _usuariosRegistrados
from model.Usuario import Usuario
user = Usuario('', '',
               '', '', '')


def buscarUsuario(correo):
    for usuario in _usuariosRegistrados:
        if usuario.correo == correo:
            user.nombre = usuario.nombre
            user.apellido = usuario.apellido
            user.correo = usuario.correo
            user.password = usuario.password
            user.nivelUsu = usuario.nivelUsu
            return True


def validarContrasenia(password):

    if user.password == str(password):
        print('BIENVENIDO')
        return True
