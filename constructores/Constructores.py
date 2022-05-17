from model.Usuario import Usuario
from model.Auto import Auto
from data.Usuarios import agregaUsuarios, printUsuarios
from data.Auto import agregaAutos


def crearUsuarios():
    usuario = Usuario('Lionel', 'Messi',
                      'alexis.lorda@ites.com', '1', 3)
    agregaUsuarios(usuario)
    usuario = Usuario('Lewis', 'Hamilton',
                      'lewis.hamilton@ites.com', '1', 2)
    agregaUsuarios(usuario)
    usuario = Usuario('Jhon', 'Travolta',
                      'jhon.travolta@ites.com', 'alexis', 1)
    agregaUsuarios(usuario)


def crearAuto():
    auto = Auto('VW', 'Gol', 15225, 'Muy bonito')
    agregaAutos(auto)
    auto = Auto('Ferrari', 'FF', 0, 'Un lujo')
    agregaAutos(auto)


def insertarAuto():
    marca = input('Ingrese la marca: ')
    modelo = input('Ingrese la modelo:')
    km = input('Ingrese el kilometraje: ')
    detalle = input('Ingrese los detalles')
    auto_ingresado = Auto(marca, modelo,  km, detalle)
    agregaAutos(auto_ingresado)
