 #!/usr/bin/env python

"""
    talk.py 
    
    Use the sound_play client to answer what is heard by the pocketsphinx recognizer.
    
"""

import rospy, os, sys
from std_msgs.msg import String
from sound_play.libsoundplay import SoundClient

class TalkBot:
     def __init__(self, script_path):
         rospy.init_node('talk')

         rospy.on_shutdown(self.cleanup)

         # Create the sound client object
         #self.soundhandle = SoundClient()
         self.soundhandle = SoundClient(blocking=True)

         # Wait a moment to let the client connect to the sound_play server
         rospy.sleep(1)

         # Make sure any lingering sound_play processes are stopped.
         self.soundhandle.stopAll()

         
         #Announce that we are ready
         self.soundhandle.say('Hello, I am John. What can I do for you?',volume=0.03)
         rospy.sleep(3)

         rospy.loginfo("Say one of the navigation commands...")

         # Subscribe to the recognizer output and set the callback function
         rospy.Subscriber('/lm_data', String, self.talkback)
         

     def talkback(self, msg):
         #Print the recognized words on the screen
         rospy.loginfo(msg.data)

         if msg.data.find('HOW-OLD-ARE-YOU')>-1:
             rospy.loginfo("Talk: I am twenty-one years old.")
             self.soundhandle.say("I am twenty-one years old.", volume=0.03)
             #rospy.sleep(2)
         elif msg.data.find('COLOR-YOU-LIKE')>-1:
             rospy.loginfo("Talk: OK. I like red best")
             self.soundhandle.say("I like red best.", volume=0.03)
	     #rospy.sleep(2)
         elif msg.data.find('ARE-YOU-FROM')>-1:
             rospy.loginfo("Talk: I am from  China.")
             self.soundhandle.say("I am from China.", volume=0.03)
             #rospy.sleep(2)
         elif msg.data.find('SPORT-YOU-LIKE')>-1:
             rospy.loginfo("Talk: I like playing cooking.")
             self.soundhandle.say("I like playing cooking.", volume=0.03)
             #rospy.sleep(2)
         elif msg.data.find('INTRODUCE-YOURSELF')>-1:
             rospy.loginfo("Talk: I am  john, a service robot.")
             self.soundhandle.say("I am john, a service robot.", volume=0.03)
             #rospy.sleep(2)
         elif msg.data=='':
             rospy.sleep(1)
         else:
             rospy.loginfo("Talk: Sorry I can not understand,can you repeat it?")
             self.soundhandle.say("Sorry I can not understand,can you repeat it?", volume=0.03)
             #rospy.sleep(3)

     def cleanup(self):
         self.soundhandle.stopAll()
         rospy.loginfo("Shutting down talkbot node...")

if __name__=="__main__":
    try:
        TalkBot(sys.path[0])
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Talk node terminated.")

