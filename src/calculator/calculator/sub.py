#!/usr/bin/env python3

# ^ a shabang, tells where to find python3

import rclpy # ros python library
from rclpy.node import Node # this is a ros node
from std_msgs.msg import Float32MultiArray # ROS standard message type Float32MultiArray


# subscribers are handled as a class, inherited from Node.
class Subscriber(Node):
    # initialisation
    def __init__(self):
        super().__init__("simple_subscriber") # ROS' super initialisation function from Node.
        self.subscription = self.create_subscription(Float32MultiArray, "number_topic", self.callback_func, 10) # create self.publisher, for data type, data channel (rostopic), callback, and queue size

    # function that will be run whenever a new message is published to the channel
    def callback_func(self, msg):
        sum = 0.0
        for num in msg.data:
            sum += num
        self.get_logger().info("The sum is: %s" % sum) # prints info to terminal in a standardised ROS format

def main():
    rclpy.init(args=None) # initialise ROS network
    listener = Subscriber() # create subscriber
    rclpy.spin(listener) # run subscriber indefinitely

if __name__ == "__main__":
    main()