class Signal:
  def __init__(self,
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
    self.id = None
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

  def toJSON(self):
    return {
      'userId': self.userId,
      'zoneId': self.zoneId,
      'color': self.color,
      'effect': self.effect,
      'isArchived': self.isArchived,
      'isMuted': self.isMuted,
      'isRead': self.isRead,
      'shouldNotify': self.shouldNotify,
      'pid': self.pid,
      'clientName': self.clientName,
      'message': self.message,
      'name': self.name
    }

