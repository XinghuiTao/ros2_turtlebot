from interfaces.srv import Move
import rclpy
from rclpy.node import Node
import sys


class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.client = self.create_client(Move, 'movement')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        
        self.req = Move.Request()
        

    def send_request(self):
        self.req.move = sys.argv[1]
        self.future = self.client.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)
    client = Client()
    client.send_request()

    while rclpy.ok():
        rclpy.spin_once(client)
        if client.future.done():
            try:
                response = client.future.result()
            except Exception as e:
                client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                client.get_logger().info(
                    'Response state %r' % (response.success,))
            break

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()