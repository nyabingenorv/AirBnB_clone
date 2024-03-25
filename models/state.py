#!/usr/bin/python3
"""The state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    child classs of BaseModel
    represents a state, takes one atrr - name of the state
    """
    name = ""
