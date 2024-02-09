#!/usr/bin/python3
import uuid
from datetime import datetime
#when i test it return unarrangete values
# i will investigate in it
import models

class BaseModel():
    """
    class BaseModel that defines all common
    attributes/methods for other classe
    """
    def __init__(self, *args, **kwargs):
        """
        Public instance attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "updated_at":
                        self.updated_at = datetime.fromisoformat(value)
                    elif key == "created_at":
                        self.created_at = datetime.fromisoformat(value)
                    else:
                        setattr(self, key, value)


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
        models.storage.save()
