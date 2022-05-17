from constructores.Constructores import insertarAuto
from ui.Views import *
from controller.UsuariosControllers import buscarUsuario, validarContrasenia, menu
from constructores.Constructores import insertarAuto

bienvenida()
userOk = buscarUsuario(msjUsuario())
intentos = 3
try:
    if(userOk):

        usuarioconPass = validarContrasenia(msjPassword())
        while userOk:
            if(usuarioconPass[0]):
                userOk = menu(usuarioconPass[1])
    else:
        print('No se encontro el Usuario')

finally:
    print('Gracias por Visitarnos')
