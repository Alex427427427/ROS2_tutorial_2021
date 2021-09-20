#!/usr/bin/env python3

# ^ a shabang, tells where to find python3

import rclpy # ros python library
from rclpy.node import Node # this is a ros node
from std_msgs.msg import String # ROS standard message type String


# publishers are handled as a class, inherited from Node.
class Publisher(Node):
    # initialisation
    def __init__(self):
        super().__init__("simple_publisher") # ROS' super initialisation function from Node.
        self.publisher = self.create_publisher(String, "string_topic", 10) # create self.publisher, for data type, data channel (rostopic), and data quality (10 stands for something we don't need to know)
        self.count = 0
        self.timer = self.create_timer(0.5, self.callback_func) # creates a timer that runs a function every once this interval.

    # function that will be run according to self.timer
    def callback_func(self):
        msg = String() # create message
        self.count += 1
        msg.data = "Hello world: " + str(self.count) # set message data
        self.publisher.publish(msg) # publish message
        self.get_logger().info("Publishing: " + str(msg.data)) # log to terminal in a standardised ROS format

def main():
    rclpy.init(args=None) # initialise ROS network
    talker = Publisher() # create publisher
    rclpy.spin(talker) # run publisher indefinitely

    talker.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()