import http.client
import urllib.parse
import json
## This class is used to connect to the App throught Http client
class AppApiConnection:
  def __init__(self):
    # HTTPConnection instance
    self.connection = None
    # Url that contain the ressources
    self.signal_resource_url = "/api/1.0/signals"

  def start_qapp_connection(self):
    """
    starts the http connection with localhost at the PORT Number 27301
    """
    self.connection = http.client.HTTPConnection("localhost", 27301)
  
  def is_connected_to_app(self):
    """
    returns the connection state with the App

    ensure:
    - true if the app is connected to localhost
    - false otherwise
    """
    if self.connection:
      return True
    else:
      return False

  def get_shadow_signals(self):
    """
      gets all the shadow signals from the QApp and create signal object
    """
    self.connection.request('GET', self.signal_resource_url)
    response = self.connection.getresponse()
    return response.read()

  def createSignal(self, signal):
    """
      send a signal to the app via POST request
    """
    signal_json = signal.toJSON()
    signal_json = json.dumps(signal_json)
    headers = {"Content-type": "application/json", "cachee-control": "no-cache"}
    self.connection.request('POST',self.signal_resource_url,signal_json,headers)
    response = self.connection.getresponse()