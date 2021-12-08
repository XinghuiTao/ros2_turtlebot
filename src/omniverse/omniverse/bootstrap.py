import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import ReliabilityPolicy, QoSProfile
from messager.msg import Date

class Bootstrap(Node):

    def __init__(self):
        super().__init__('Bootstrap')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber = self.create_subscription(LaserScan, '/scan', self.move_turtlebot, QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
        # prevent unused variable warning
        self.subscriber
        # define the timer period for 0.5 seconds
        self.timer_period = 0.5
        # define the variable to save the received info
        self.laser_forward = 0
        # create a Twist message
        self.cmd = Twist()
        self.timer = self.create_timer(self.timer_period, self.motion)

    def move_turtlebot(self,msg):
        # Save the frontal laser scan info at 0°
        self.laser_forward = msg.ranges[359] 

    def motion(self):
        # print the data
        self.get_logger().info('I receive: "%s"' % str(self.laser_forward))
        # Logic of move
        if self.laser_forward > 5:
            self.cmd.linear.x = 0.5
            self.cmd.angular.z = 0.5
        elif self.laser_forward <5 and self.laser_forward>=0.5:
            self.cmd.linear.x = 0.2
            self.cmd.angular.z = 0.0   
        else:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.0
        # Publishing the cmd_vel values to topipc
        self.publisher_.publish(self.cmd)

            
def main(args=None):
    rclpy.init(args=args)
    bootstrap = Bootstrap()       
    rclpy.spin(bootstrap)
    bootstrap.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()