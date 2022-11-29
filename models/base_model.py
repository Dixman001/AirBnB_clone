#!/usr/bin/python3
'''this module serves as the base of the project'''

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    ''' '''

    def __init__(self):
        '''initializing the ins and att'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        '''returns string representation'''

        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        ''' '''

        self.updated_at = datetime.(now)
        storage.save()

    def to_dict(self):
        '''returns a dictionary'''

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
