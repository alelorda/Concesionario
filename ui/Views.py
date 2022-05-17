from constructores.Constructores import crearUsuarios, crearAuto


def bienvenida():
    print('Bienvenidos a Concesionaria "Rayo McQueen"'.center(1000))
    crearUsuarios()
    crearAuto()


def msjUsuario():
    return input('Ingrese Correo Electronico: ')


def msjErrorUsuario():
    print('Usuario Incorrecto')


def msjPassword():
    return input('Ingrese Password: ')


def msjErrorPassword():
    print('Password Incorrecta')
