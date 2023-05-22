#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
import models
from sqlalchemy.orm import relationship, backref
import os

class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                              cascade="all, delete, delete-orphan",
                              backref="state")

    @property
    def cities(self):
        """Return list of cities"""
        city_list = [value for key, value in
                         models.storage.all(City).items()
                         if value.state_id == self.id]
        return city_list
