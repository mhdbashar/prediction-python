# import pandas as pd
import numpy as np
from lib.prediction import *
import re

# grpc
import grpc
from concurrent.futures import ThreadPoolExecutor
from lib.grpc.prediction_pb2 import PredictionRequest, PredictionResponse
from lib.grpc.prediction_pb2_grpc import PredictionServiceServicer, add_PredictionServiceServicer_to_server

#config
orig_r=4
orig_c=7

#two hour in three day before
wind_r=2
wind_c=3

microservices_ts= {}
microservices_cfg= {}

def update_microservices_ts(key, value):
    # if key in microservices_ts:
    #     # diff=list(set(microservices_ts[key])-set(value))
    #     microservices_ts[key].extend(diff)  # If the key exists, append to the existing array
    # else:
    microservices_ts[key] = value # If the key doesn't exist, create a new array with the value

def update_microservices_cfg(key,history=orig_r,stepDuration=15,predictVerticalWindow=wind_r,predictHorizontalWindow=wind_c):
      microservices_cfg[key] = {
        "orig_r":int(re.search(r'\d+', history).group()), #orig_r
        "orig_c":int(60*24/int(re.search(r'\d+', stepDuration).group())), #orig_c
        "wind_r":int(predictVerticalWindow), #wind_r
        "wind_c":int(predictHorizontalWindow) #wind_c
        }  # If the key doesn't exist, create a new array with the value


class PredictionServiceImpl(PredictionServiceServicer):
    def ProcessData(self, request, context):
        # Process the received arrays and strings
        microservice = request.micorservice_name
        update_microservices_ts(microservice,request.measurements)
        update_microservices_cfg(microservice,request.history,request.stepDuration,request.predictVerticalWindow,request.predictHorizontalWindow)
        print(microservices_ts)
        # print(microservices_cfg)
        response=prediction(microservices_ts[microservice],microservices_cfg[microservice]["orig_r"],microservices_cfg[microservice]["orig_c"],microservices_cfg[microservice]["wind_r"],microservices_cfg[microservice]["wind_c"])
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
