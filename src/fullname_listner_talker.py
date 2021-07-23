#!usr/bin/env python
from os import strerror
import rospy 
from std_msgs.msg import String
from ros_a1.msg import name_pub


np=name_pub()


    
            
li=['','']

def call_back1(msg):
    rospy.loginfo(msg.data)
    np.first_name = msg.data
    
    
    

def call_back2(msg):
    rospy.loginfo(msg.data)
    np.second_name= msg.data
    return surname_rec
    
    


rospy.init_node('fullname_listner_talker',anonymous=True)
rospy.Subscriber('name',String,call_back)
rospy.Subscriber('surname',String,call_back)
pub = rospy.Publisher('fullname',name_pub,queue_size=10)
rospy.spin()