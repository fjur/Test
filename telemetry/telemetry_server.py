""" The python implementation of the telemetry server"""

from concurrent import futures
import time

import grpc

# from test import telemetry_pb2_grpc
from protos import telemetry_pb2_grpc

# python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/telemetry.proto

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class TelemetryServicer(telemetry_pb2_grpc.TelemetryServicer):
    """provides methods that implement the telemetry servicer"""

    def __init__(self):
        self.logs = {}
        self.logId = 0

    def GetLog(self, request, context):
        logId = request.logId
        logMessage = self.logs[logId]
        log = telemetry_pb2.Log()
        log.logMessage = logMessage
        return log

    def AddLog(self, request, context):
        print(self)
        self.logId += 1
        self.logs[self.logId] = request.logMessage
        return telemetry_pb2.LogId(logId=self.logId)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    telemetry_pb2_grpc.add_TelemetryServicer_to_server(TelemetryServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    print("Server has begun")

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()