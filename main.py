from constructores.Constructores import insertarAuto
from ui.Views import *
from controller.UsuariosControllers import buscarUsuario, validarContrasenia
from constructores.Constructores import insertarAuto

bienvenida()
userOk = buscarUsuario(msjUsuario())

if(userOk):

    passOk = validarContrasenia(msjPassword())
    # if(not msjErrorPassword):

else:
    print('No se encontro el Usuario')
