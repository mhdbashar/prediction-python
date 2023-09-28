# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import lib.grpc.prediction_pb2 as prediction__pb2


class PredictionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessData = channel.unary_unary(
                '/prediction.PredictionService/ProcessData',
                request_serializer=prediction__pb2.PredictionRequest.SerializeToString,
                response_deserializer=prediction__pb2.PredictionResponse.FromString,
                )


class PredictionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessData': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessData,
                    request_deserializer=prediction__pb2.PredictionRequest.FromString,
                    response_serializer=prediction__pb2.PredictionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prediction.PredictionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PredictionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prediction.PredictionService/ProcessData',
            prediction__pb2.PredictionRequest.SerializeToString,
            prediction__pb2.PredictionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
