from . import api
from .resources.home import Get_List


api.add_resource(Get_List, '/api/list')