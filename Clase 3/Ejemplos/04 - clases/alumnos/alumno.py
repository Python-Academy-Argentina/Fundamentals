import json


class Alumno:
    '''
    Una simple clase que representa a un alumno.
    '''

    def __init__(self, nombre, apellido, notas=None, id_=None):

        self.id = id_
        self.nombre = nombre
        self.apellido = apellido
        self.__notas = notas or []

    def __repr__(self):
        return f'<ID: {self.id} - Apellido: {self.apellido}>'

    def __str__(self):
        promedio = round(self.promedio(), 1)

        return f'ID: {self.id}; Alumno: {self.nombre_completo}; Promedio: {promedio}'
    
    @property
    def nombre_completo(self):
        '''
        Devuelve el nombre completo en formato <apellido, nombre>.
        '''
        return f'{self.apellido}, {self.nombre}'

    @property
    def notas(self):
        '''
        Devuelve la lista de notas.
        '''
        return self.__notas

    def agregar_nota(self, nota):
        '''
        Agrega una nota a self.__notas.
        '''
        self.__notas.append(nota)

    def borrar_nota(self, indice):
        '''
        Borra una nota de self.__notas.
        '''
        del self.__notas[indice]

    def promedio(self):
        '''
        Devuelve el promedio de self.__notas.
        '''
        try:
            promedio = sum(self.__notas) / len(self.__notas)
        except ZeroDivisionError:
            promedio = 0

        return promedio

    def a_json(self):
        '''
        Devuelve un JSON-string con los datos del alumno.
        '''
        datos = {
            'id_': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'notas': self.__notas
        }
        return json.dumps(datos)

    @classmethod
    def desde_json(cls, json_str):
        '''
        Devuelve un objeto Alumno a partir de un JSON-string.
        '''
        return cls(**json.loads(json_str))
