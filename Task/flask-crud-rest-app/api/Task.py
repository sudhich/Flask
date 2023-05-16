from flask_restful import Resource
import logging as logger


class Task(Resource):

    def get(self):
        logger.debug("Inside the Get method")
        return {"message" : "Insite Get method"}, 200

    def post(self):
        logger.debug("Inside the Post method")
        return {"message": "Insite Post method"}, 200

    def put(self):
        logger.debug("Inside the Put method")
        return {"message": "Insite Put method"}, 200

    def delete(self):
        logger.debug("Inside the Delete method")
        return {"message": "Insite Delete method"}, 200
