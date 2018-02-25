# server/models.py
from flask_sqlalchemy.model import BindMetaMixin
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy_mixins import AllFeaturesMixin


class NoNameMeta(BindMetaMixin, DeclarativeMeta):
    """
    Custom MetaData to disable default tablename generation
    Supports bind_keys to for multiple database
    """
    pass


Base = declarative_base(metaclass=NoNameMeta, name="Model")


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True
