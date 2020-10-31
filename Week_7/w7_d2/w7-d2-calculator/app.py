# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Calculator(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create pair arguments
        parser.add_argument('operation', type=str)
        operation_name = parser.parse_args().get('operation')

        parser.add_argument('num1', type=int)
        num1 = parser.parse_args().get('num1')

        parser.add_argument('num2', type=int)      
        num2 = parser.parse_args().get('num2')

        if operation_name == 'add':
            result = num1 + num2
        elif operation_name == 'substract':
            result = num1 - num2
        elif operation_name == 'divide':
            result = num1 / num2
        elif operation_name == 'multiply':
            result = num1 * num2
        else:
            result = 'invalid operation, please use add,substract,multiply,divide and please no division by 0'

        # make json from greeting string 
        return jsonify(result=result)

# assign endpoint
api.add_resource(Calculator, '/calculator',)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
#http://0.0.0.0:5001/calculator?operation=add&num=69&num2=420\