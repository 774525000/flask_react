from flask_restful import Resource


class Get_List(Resource):
	def get(self):
		return { 'name': 'shuaige'}