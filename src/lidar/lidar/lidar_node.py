#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_node')
        self.publisher = self.create_publisher(String, 'salut_fm', 10)
        self.timer = self.create_timer(1.0, self.send_warning)

    def send_warning(self):
        msg = String()
        msg.data = 'Впереди стена! Ахтунг! Алярм!'
        self.publisher.publish(msg)
        self.get_logger().info(msg.data)


def main():
    rclpy.init()
    node = LidarNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Нода с лидаром выключена')
    finally:
        node.destroy_node()