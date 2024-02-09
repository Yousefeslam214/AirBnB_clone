#!/usr/bin/python3
import uuid
from datetime import datetime
#when i test it return unarrangete values
# i will investigate in it
from __init__ import storage


class BaseModel():
    """
    class BaseModel that defines all common
    attributes/methods for other classe
    """
    def __init__(self, *args, **kwargs):
        """
        Public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return


    def __str__(self):
        """
        should print:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            type(self).__name__,self.id, self.__dict__
        )

    def to_dict(self):
        """Public instance methods"""
        dict = {**self.__dict__} # id created_at updated_at
        dict['__class__'] = type(self).__name__ # BaseModel
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict

    def save(self):
        """Public instance methods"""
        self.updated_at = datetime.now()
        storage.save()
