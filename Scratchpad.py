class Sensor:
  def __init__(self, name):
    """
    Initializes a sensor object while giving it a name
    """
    self._name = name

  def get_name(self):
    return self._name

class CustomizableRobot:
  def __init__(self, name):
    """
    Initializes a robot while giving it a name
    """
    self._name = name #the name of this robot
    self._sensors = [] #a list that will contain the sensors later on
    self._actuators = []  #a list that will contain the actuators later on
    self._state = "off" #whether it's on or off
    self._operating_system = "Linux"

  def install_sensor(self, sensor_object):
    """
    Install the given sensor object by adding to the list of sensors for the robot
    """
    print("Installing sensor ", sensor_object.get_name())
    self._sensors.append(sensor_object)

  def remove_sensor(self, sensor_object):
    """
    Removes the given sensor by removing it from the list of sensors for the robot
    """
    print("Removing sensor ", sensor_object.get_name())
    self._sensors.remove(sensor_object)


#Creates an object of the CustomizableRobot class
walle_robot_object = CustomizableRobot("WALL-E")

#Creates Sensor objects
camera_sensor = Sensor("3D Camera")
mic_sensor = Sensor("Microphone")

#Install the sensors
walle_robot_object.install_sensor(camera_sensor)
walle_robot_object.install_sensor(mic_sensor)

#Remove the sensor
walle_robot_object.remove_sensor(camera_sensor)