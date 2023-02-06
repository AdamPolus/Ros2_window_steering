import pygame
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class SubNode(Node):
    def __init__(self):
        super().__init__("window_control")  
        self.cmd_vel_pub_=self.create_publisher(
            Twist,"/turtle1/cmd_vel",10) 
        self.pose_sub=self.create_subscription(
            Pose,"/turtle1/pose",self.pose_cb,10) 
    
    def pose_cb(self,pose:Pose):
        cmd=Twist()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
            # get the mouse click position
                global pos
                pos = pygame.mouse.get_pos()
                print(pos)
            # update the screen
                pygame.display.update()
        self.get_logger().info("initializating control command")
        
        if pos[1]>400 and pos[0]<400:
            self.get_logger().info("go up")
            cmd.linear.x=2.0
        elif pos[1]<400 and pos[0]<400:
            cmd.linear.x=-2.0
            self.get_logger().info("go down")
        elif pos[0]>400 and pos[1]>400:
            self.get_logger().info("go left-side")
            cmd.linear.y=2.0
        elif pos[0]>400 and pos[1]<400:
            self.get_logger().info("go right-side")
            cmd.linear.y=-2.0
        self.cmd_vel_pub_.publish(cmd)

# initialize pygame library
pygame.init()

# set screen size
screen = pygame.display.set_mode((800, 800))

# set screen title
pygame.display.set_caption("Window for controllin TurtleSIM")

def main(args=None): 
    rclpy.init(args=args)
    node=SubNode()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__=='__main__':
    main()

