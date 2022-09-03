#!/usr/bin/python3
"""
Has the class BaseModel
"""

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
	"""This the BaseModel class that will derive future classes"""
	
	def __init__(self, *arg, **kwargs):
		"""
		It creates a new instance of the class.
		"""
		time = "%Y-%m-%dT%H:%M:%S.%f"
	   	self.id = str(uuid4())
	        self.created_at = datetime.now()
	        self.updated_at = datetime.now()
	        if len(kwargs) != 0:
	 for 
	 	  
