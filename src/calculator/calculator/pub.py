#!/usr/bin/env python3

# ^ a shabang, tells where to find python3

import rclpy # ros python library
from rclpy.node import Node # this is a ros node
from std_msgs.msg import Float32MultiArray # ROS standard message type Float32MultiArray


# publishers are handled as a class, inherited from Node.
class Publisher(Node):
    # initialisation
    def __init__(self):
        super().__init__("simple_publisher") # ROS' super initialisation function from Node.
        self.publisher = self.create_publisher(Float32MultiArray, "number_topic", 10) # create self.publisher, for data type, data channel (rostopic), and data quality (10 stands for something we don't need to know)
        self.timer = self.create_timer(0.5, self.callback_func) # creates a timer that runs a function every once this interval.

    # function that will be run according to self.timer
    def callback_func(self):
        try:
            msg = Float32MultiArray() # create message
            msg.data.append(float(input("Enter your first number: "))) # set message data
            msg.data.append(float(input("Enter your second number: ")))
            self.publisher.publish(msg) # publish message
        except:
            self.get_logger().info("That wasn't a number! Try again.")

def main():
    rclpy.init(args=None) # initialise ROS network
    talker = Publisher() # create publisher
    rclpy.spin(talker) # run publisher indefinitely

    talker.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()