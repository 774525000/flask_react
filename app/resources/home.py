from flask_restful import Resource
from flask import request


class Get_List(Resource):
	def get(self):
		return { 'name': 'shuaige'}

	def post(self):
		print(request.form['name'])
		return {'age': 18}