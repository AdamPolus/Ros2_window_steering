import rclpy
from getch import getch
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class SubNode(Node):
    def __init__(self):
        super().__init__("key_control")  
        self.cmd_vel_pub_=self.create_publisher(
            Twist,"/turtle1/cmd_vel",10) 
        self.pose_sub=self.create_subscription(
            Pose,"/turtle1/pose",self.pose_cb,10) 
    
    
    def pose_cb(self,pose:Pose):
        cmd=Twist()
        self.get_logger().info("start control")
        key=getch()
        if key=='w':
            self.get_logger().info("for")
            cmd.linear.x=2.0
        elif key=='s':
            cmd.linear.x=-2.0
            self.get_logger().info("back")
        elif key=='a':
            self.get_logger().info("left")
            cmd.angular.z=2.0
        elif key=='d':
            self.get_logger().info("right")
            cmd.angular.z=-2.0
        self.cmd_vel_pub_.publish(cmd)
        

def main(args=None): 
    rclpy.init(args=args)
    node=SubNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
