import rospy, cv2
from sensor_msgs.msg import Image
import sys

sys.path.append("~/catkin_workspace/install/lib/python3/dist-packages/")
import cv_bridge


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        # cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('/camera/zed/rgb/image_rect_color',
                                          Image, self.image_callback)
        self.num1 = 68
        self.num2 = 68

    def image_callback(self, msg):
        self.image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        cv2.imshow("pic", self.image)
        k = cv2.waitKey(3)
        if k == 27:  # 按ESC退出
            cv2.destroyAllWindows()

        elif k == ord('r'):  # 按r保存并退出
            self.num1 += 1
            cv2.imwrite("./red/" + str(self.num1) + ".jpg", self.image)
            print("红色保存成功：" + str(self.num1) + ".jpg")

        elif k == ord('g'):  # 按r保存并退出
            self.num2 += 1
            cv2.imwrite("./green/" + str(self.num2) + ".jpg", self.image)
            print("绿色保存成功：" + str(self.num2) + ".jpg")


if __name__ == '__main__':
    rospy.init_node('follower')
    follower = Follower()
    rospy.spin()