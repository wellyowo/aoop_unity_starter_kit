#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

from siege_game.game_objects.logger import Logger

class ServerDetectClientAListener(rospy.SubscribeListener):
    logger = Logger("ServerDetectClientAListener")
    def __init__(self, __game_data_publisher):
        self.__game_data_publisher:GameDataPublisher = __game_data_publisher

    def peer_subscribe(self, topic_name, topic_publish, peer_publish):
        ServerDetectClientAListener.logger.info("A peer subscribed to topic [%s]"%topic_name)
        peer_publish(String(str))
        
    def peer_unsubscribe(self, topic_name, numPeers):
        ServerDetectClientAListener.logger.info("A peer unsubscribed from topic [%s]"%topic_name)
        ServerDetectClientAListener.logger.fatal("BOOOM")
        self.__game_data_publisher.boomClientA()
        self.__game_data_publisher.boomClientB()
        

class GameDataPublisher:
    logger = Logger('GameDataPublisher')

    def __init__(self):
        GameDataPublisher.logger.warning("<game_data_publisher.py> Use get_instance class method to obtain the instance")
        self.__server_signin_publisher = rospy.Publisher('/server_signin', String, queue_size=10)
        self.__server_signin_message = String()

        self.__server_detect_client_A = rospy.Publisher('/server_detect_client_A', String, queue_size=50, subscriber_listener=ServerDetectClientAListener())
        self.__server_detect_client_A_data = String()
        self.__server_detect_client_A_data.data = "safe"

        self.__server_detect_client_B = rospy.Publisher('/server_detect_client_B', String, queue_size=50, subscriber_listener=ServerDetectClientAListener())
        self.__server_detect_client_B_data = String()
        self.__server_detect_client_B_data.data = "safe"
    
    def publish_server_signin(self, id, msg):
        full_msg = f"{id} {msg}"
        self.__server_signin_message.data = full_msg
        GameDataPublisher.logger.info(f"Sending data to server signin channel: {full_msg}")
        self.__server_signin_publisher.publish(self.__server_signin_message)

    def boomClientA(self):
        self.__server_detect_client_A_data.data = "boom"

    def publishDetectClientA(self):
        self.__server_detect_client_A(self.__server_detect_client_A_data)

    def boomClientB(self):
        self.__server_detect_client_B_data.data = "boom"

    def publishDetectClientB(self):
        self.__server_detect_client_B(self.__server_detect_client_B_data)

    

