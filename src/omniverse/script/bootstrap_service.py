from std_srvs.srv import SetBool
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class Service(Node):
    def __init__(self):
        super().__init__('service')
        self.srv = self.create_service(SetBool, 'moving', self.SetBool_callback)
       
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.cmd = Twist()

    def SetBool_callback(self, request, response):
        if request.data == True:            
            self.cmd.linear.x = 0.3
            self.cmd.angular.z =-0.3
            
            self.publisher_.publish(self.cmd)
            response.success = True
            response.message = 'MOVING TO THE RIGHT RIGHT RIGHT!'

        if request.data == False:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z =0.0
            
            self.publisher_.publish(self.cmd)
            response.success = False
            response.message = 'It is time to stop!'


        return response

def main(args=None):
    rclpy.init(args=args)
    moving_right_service = Service()
    rclpy.spin(moving_right_service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()