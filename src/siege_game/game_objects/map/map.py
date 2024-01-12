#!/usr/bin/env python3
# import rospy
# from std_msgs.msg import UInt8MultiArray
# from sensor_msgs.msg import Mouse
from siege_game.game_objects.map_data_processor import MapDataProcessor
from siege_game.game_objects.game_data_publisher import GameDataPublisher
from siege_game.game_objects.game_flow_director import GameFlowDirector
from collections import deque
from siege_game.game_objects.pawn.attaker import Attacker
from siege_game.game_objects.pawn.defender import Defender
from siege_game.game_objects.player import Player
import json
import logging

class Map:
    logger = logging.getLogger('map')
    """
    Map is where the battle situated

    Attributes:
        __map (dict): key is (x, y) and value is map object
        __map_width (int): the width of the map
        __map_height (int): the height of the map
        __defend_player (Player): The real player who is the defending side
        __attack_player (Player): The real player who is the attacking side
        __defenders (deque):  contains operators who is defending the map
        __attackers (deque):  contains operators who is attacking the map
        __map_data_processor: an object which process the map into two maps for two players
        __game_data_publisher: an object which get the data and sent the data to the client unity side
        __game_flow_director: an object which is the main judge of the game
    """

    def __init__(self, map:dict, map_width:int, map_height:int, defend_player:Player, attack_player:Player, defender_count:int, attacker_count:int):
        """
        Don't use constructor to init this class, use get_instance method instead

        Attributes:
            map (dict): a dict that its keys are location and values are map objects
            map_width (int): the width of the map
            map_height (int): the height of the map
            defend_player (Player): The real player who is the defend team
            attack_player (Player): The real player who is the attacking side
            defender_count (int): The count of the operators who is defending the map. Default is 5 operators
            attacker_count (int): The count of the operators who is attacking the map. Default is 5 operators

        Returns:
            Dont use this thing you XXXXXX
        """
        Map.logger.warning("<map.py> Use get_instance class method to obtain the instance")
        self.__map = map
        self.__defend_player = defend_player
        self.__attack_player = attack_player
        self.__defenders = deque()
        self.__attackers = deque()
        self.__map_width = map_width
        self.__map_height = map_height
        self.__map_data_processor = MapDataProcessor()
        self.__game_data_publisher = GameDataPublisher()
        self.__game_flow_director = GameFlowDirector()

        for _ in range(defender_count):
            self.__defenders.append(Defender(self.__defend_player))

        for _ in range(attacker_count):
            self.__attackers.append(Attacker(self.__attack_player))
    
    def print_map(self):
        Map.logger.info(f"Printing the current map... (Size: {self.__map_width} * {self.__map_height})")
        for y in range(self.__map_height):
            for x in range(self.__map_width):
                print('{0:<20}'.format(f'{self.__map[(x, y)]}'), end=" ")
            print()
            


        # self.map_publisher = rospy.Publisher('/map_information', UInt8MultiArray, queue_size=1)
        # self.attacker_mouse_subsriber = rospy.Subscriber('/attacker_mouse_event', UInt8MultiArray, self.attacker_mouse_callback)
        # self.defender_mouse_subsriber = rospy.Subscriber('/defender_mouse_event', UInt8MultiArray, self.defender_mouse_callback)
        # self.map_message = UInt8MultiArray()



    # def attacker_mouse_callback(self, message):
    #     print("message")
    #     print(type(message))

    # def defender_mouse_callback(self, message):
    #     print("message")
    #     print(type(message))