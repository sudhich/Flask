from flask_restful import Resource
import logging as logger


class TaskById(Resource):

    def get(self,TaskId):
        logger.debug("Inside the Get method Task by Id")
        return {"message" : "Insite Get method Task by Id. TASK_ID={}".format(TaskId)}, 200

    def post(self,TaskId):
        logger.debug("Inside the Post method Task by Id")
        return {"message": "Insite Post method Task by Id. TASK_ID={}".format(TaskId)}, 200

    def put(self,TaskId):
        logger.debug("Inside the Put method Task by Id")
        return {"message": "Insite Put method Task by Id. TASK_ID={}".format(TaskId)}, 200

    def delete(self,TaskId):
        logger.debug("Inside the Delete method Task by Id")
        return {"message": "Insite Delete method Task by Id. TASK_ID={}".format(TaskId)}, 200
