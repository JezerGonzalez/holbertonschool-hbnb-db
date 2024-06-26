"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base
from src.persistence.repository import Repository
from flask import current_app as app


class DBRepository(Repository):
    """Dummy DB repository"""

    def __init__(self) -> None:
        """Sets the configuration as the app"""
        self.useData = app.config['USE_DATABASE']

    def get_all(self, model_name: str) -> list:
        """Gets all models in the database"""
        if self.useData:
            return app.db.session.query(model_name).all()
        else:
            return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Returns data for the given model"""
        if self.useData:
            return app.db.session.query(model_name).filter_by(id=obj_id).first()
        else:
            return None

    def reload(self) -> None:
        """Not implemented"""

    def save(self, obj: Base) -> None:
        """Saves the given model"""
        if self.useData:
            app.db.session.add(obj)
            app.db.session.commit()
        else:
            pass

    def update(self, obj: Base) -> Base | None:
        """Updates the given model"""
        if self.useData:
            app.db.session.add(obj)
            app.db.session.commit()
            return obj
        else:
            return None

    def delete(self, obj: Base) -> bool:
        """Deletes the given model"""
        if self.useData:
            app.db.session.delete(obj)
            app.db.session.commit()
            return True
        else:
            return False
