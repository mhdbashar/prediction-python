# import pandas as pd
import numpy as np
from lib.prediction import prediction
from lib.helper import *

# grpc
import grpc
from concurrent.futures import ThreadPoolExecutor
from lib.grpc.prediction_pb2 import PredictionRequest, PredictionResponse
from lib.grpc.prediction_pb2_grpc import PredictionServiceServicer, add_PredictionServiceServicer_to_server


class PredictionServiceImpl(PredictionServiceServicer):
    def ProcessData(self, request, context):
        # Process the received arrays and strings
        microservice = request.micorservice_name
        update_microservices_ts(microservice,request.measurements)
        update_microservices_cfg(microservice,request.history,request.stepDuration,request.predictVerticalWindow,request.predictHorizontalWindow)
        print(microservices_ts)
        # print(microservices_cfg)
        response=prediction(microservices_ts[microservice],microservices_cfg[microservice]["orig_r"],microservices_cfg[microservice]["orig_c"],microservices_cfg[microservice]["wind_r"],microservices_cfg[microservice]["wind_c"],"fast_dtw")
        print(int(response))
        return PredictionResponse(result=int(response))

def serve():
    server = grpc.server(ThreadPoolExecutor())
    add_PredictionServiceServicer_to_server(PredictionServiceImpl(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
