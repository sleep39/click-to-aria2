from xmlrpc.client import ServerProxy
from sys import argv

txt = argv[1]
#URLProtocol %1

tk = 'sleep39'
#your setting token

s = ServerProxy('http://localhost:6800/rpc')
s.aria2.addUri("token:"+tk,[txt])

#http://your setting ip:port/rpc
