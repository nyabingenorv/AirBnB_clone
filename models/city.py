#!/usr/bin/python3
"""The city class"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherit BaseModel
    """
    state_id = ""
    name = ""
