import requests


class Client:
    '''
    Cliente para interactuar con la PAF CRUD API.
    '''

    def __init__(self, address, port,
        id_=None,
        username=None,
        password=None,
        token=None,
        session=None
    ):

        self.address = address
        self.port = port
        self.id = id_
        self.username = username
        self.password = password
        self.token = token
        self.session = session or requests.Session()

    def __repr__(self):
        return f'<PAF API Client - URL: {self.base_url}, Username: {self.username}>'

    @property
    def base_url(self):
        '''
        Devuelve la URL base.
        '''
        return f'http://{self.address}:{self.port}/api/'

    @property
    def authorization(self):
        '''
        Devuelve el header de de autorazación.
        '''
        return {'Authorization': f'Token {self.token}'}

    def create_user(self, username, password):
        '''
        Crea un nuevo usuario.
        '''
        return self._request('POST', 'register/',
            json={'username': username, 'password': password}
        )

    def get_token(self, username=None, password=None, save=False):
        '''
        Devuelve el token del usuario.
        '''
        auth_json = {
            'username': username or self.username,
            'password': password or self.password
        }
        resp = self._request('POST', 'auth/', json=auth_json)

        if save:
            self.token = resp.json().get('token')
        
        return resp

    def get_all_users(self):
        '''
        Devuelve todos los usuarios.
        '''
        return self._request('GET', 'user/',
            headers=self.authorization
        )
    
    def search_users(self, string):
        '''
        Devuelve todos los usuarios que matchean con <string>.
        '''
        return self._request('GET', f'user?search={string}',
            headers=self.authorization
        )

    def get_user(self, user_id):
        '''
        Devuelve un usuario.
        '''
        return self._request('GET', f'user/{user_id}/',
            headers=self.authorization
        )

    def update_user(self, user_id, data):
        '''
        Actualiza un usuario y lo devuelve.
        '''
        return self._request('PATCH', f'user/{user_id}/',
            headers=self.authorization,
            json=data
        )
    
    def search_tuits(self, string):
        '''
        Devuelve todos los tuits que matchean con <string>.
        '''
        return self._request('GET', f'tuit?search={string}',
            headers=self.authorization
        )

    def get_tuit(self):
        '''
        Devuelve un tuit.
        '''
        return self._request('GET', 'tuit/',
            headers=self.authorization
        )

    def post_tuit(self, content):
        '''
        Escribe un nuevo tuit.
        '''
        return self._request('POST', 'tuit/',
            headers=self.authorization,
            json={'content': content}
        )

    def delete_tuit(self, tuit_id):
        '''
        Borra un tuit.
        '''
        return self._request('DELETE', f'tuit/{tuit_id}/',
            headers=self.authorization
        )

    def _request(self, method, endpoint, headers=None, json=None):
        '''
        Administra los HTTP requests a los distintos endpoints.
        '''
        return self.session.request(method,
            url=f'{self.base_url}{endpoint}',
            headers=headers,
            json=json
        )
