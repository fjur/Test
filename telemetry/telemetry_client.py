from protos import telemetry_pb2
from protos import telemetry_pb2_grpc
import uuid
import time
import grpc

class MessageSender():

    def __init__(self, stub):
      self.id = str(uuid.uuid4())
      self.stub = stub

    def send_messages(self):
        count = 0
        while count < 200:
            self.create_message(count)
            count += 1
            time.sleep(1)

    def create_message(self, count):
        log = telemetry_pb2.Log()
        log.logMessage = "test message {} {}".format(self.id, count)
        logId = self.stub.AddLog(log)
        print(logId)
        retrievedLog = self.stub.GetLog(logId)
        print(retrievedLog)

def serve():
    print("Client as begun")
    channel = grpc.insecure_channel('localhost:50051')
    stub = telemetry_pb2_grpc.TelemetryStub(channel)
    sender = MessageSender(stub)
    sender.send_messages()

if __name__ == '__main__':
    serve()