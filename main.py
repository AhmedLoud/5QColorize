from api import AppApiConnection
from signal import Signal

app_connection = AppApiConnection()
app_connection.start_qapp_connection()
signal = Signal(9,'KEY_T','#00FF00', 'SET_COLOR',False,False,False,True,
'DK5QPID','script','','')
app_connection.createSignal(signal)
# for i in range(255):
#   signal = Signal(9,i,'#FF0000', 'SET_COLOR', False, False, False, True, 'DK5QPID', 'script',
#   '','')
#   app_connection.createSignal(signal)