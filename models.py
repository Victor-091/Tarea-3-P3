class User:
    """Modelo de usuario para el CRUD"""
    
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email
    
    def to_dict(self):
        """Convierte el objeto User a diccionario"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
    
    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
    