from interfaces.srv import Move
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class Service(Node):
    def __init__(self):
        super().__init__('service')
        self.srv = self.create_service(Move, 'movement', self.MoveService_callback)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
    def MoveService_callback(self, request, response):
        msg = Twist()
        
        if request.move == "Turn Right":
            msg.linear.x = 0.1
            msg.angular.z = -0.5
            self.publisher_.publish(msg)
            self.get_logger().info('Turning to right direction!!')
            response.success = True
        elif request.move == "Turn Left":
            msg.linear.x = 0.1
            msg.angular.z = 0.5
            self.publisher_.publish(msg)
            self.get_logger().info('Turning to left direction!!')
            response.success = True
        elif request.move == "Stop":
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Stop there!!')
            response.success = True
        else:
            response.success = False
        
        return response

def main(args=None):
    rclpy.init(args=args)
    service = Service()
    rclpy.spin(service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()