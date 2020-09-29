import sys

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


transport = TSocket.TSocket('spark://192.168.56.1', 7077)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = ThriftHive.Client(protocol)
transport.open()
client.execute("CREATE TABLE r(a STRING, b INT, c DOUBLE)")
client.execute("LOAD TABLE LOCAL INPATH '/path' INTO TABLE r")
client.execute("SELECT * FROM r")
while (1):
 row = client.fetchOne()
 if (row == None):
     break
     print (row)



f