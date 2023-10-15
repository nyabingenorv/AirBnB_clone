#!/usr/bin/python3
"""Defines the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    child class of BaseModel
    takes 3 attributes- place_id, user_id and text
    """

    place_id = ""
    user_id = ""
    text = ""
