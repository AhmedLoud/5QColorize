from api import AppApiConnection
from signal import Signal

app_connection = AppApiConnection()
app_connection.start_qapp_connection()
signal = Signal(9,'KEY_T','#000000', 'SET_COLOR',False,False,False,True,
'DK5QPID','script','','')
print(app_connection.createSignal(signal))

for i in range(255):
  signal = Signal(9,i,'#ff0000', 'SET_COLOR', False, False, False, True, 'DK5QPID', 'script',
  '','')
  app_connection.createSignal(signal)