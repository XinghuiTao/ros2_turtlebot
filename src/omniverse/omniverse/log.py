import rclpy
from rclpy.node import Node

class Move(Node):
    def __init__(self):
        super().__init__('Move')
        self.create_timer(0.2, self.timer_callback)
        
    def timer_callback(self):
        self.get_logger().info("Moe yo Byakugan! Kore ga watashi no nindō yo")

def main(args=None):
    rclpy.init(args=args)
    node = Move()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()