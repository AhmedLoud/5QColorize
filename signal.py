class Signal:
  def __init__(self,
  id,
  userId,
  zoneId,
  color,
  effect,
  isArchived,
  isMuted,
  isRead,
  shouldNotify,
  pid,
  clientName,
  message,
  name):
    self.id = id
    self.userId = userId
    self.zoneId= zoneId
    self.color = color
    self.effect = effect
    self.isArchived = isArchived
    self.isMuted = isMuted
    self.isRead = isRead
    self.shouldNotify = shouldNotify
    self.pid = pid
    self.clientName = clientName
    self.message = message
    self.name = name

  def logSignal(self):
    print('Signal:')
    print('id:', self.id)
    print('userId', self.userId)

s = Signal(0,9,25,'#FF0000','SET_COLOR',False,False,False,False,'DK5QPID','pythonScript','',
'')
s.logSignal()

