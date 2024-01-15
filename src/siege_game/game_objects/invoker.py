import warnings
from siege_game.game import Game
import logging 
from siege_game.game_objects.player import Identity, Player

class Invoker():
    """
    Invoker class in the Command Pattern.

    The Invoker is responsible for managing and executing commands. It acts as an intermediary
    between the client and the actual command objects. It encapsulates the execution of commands,
    allowing for parameterization, queuing, and logging.

    Attributes:
        __instance (Invoker): The instance of the Invoker class.
        __commands (list): A list to store the history of executed commands.
        last_command (Command): The last executed command.

    Methods:
        get_instance(): Returns the instance of the Invoker class.
        execute(command): Execute the given command.
        undo(): Undo the last executed command.
        batch_execute(commands): Execute a batch of commands simultaneously.
    """
    logger = logging.getLogger("Invoker")
    __instance = None

    def __init__(self, game:Game) -> None:

        """
        Initialize the Invoker with an empty list to store commands.
        """
        warnings.warn("Use get_instance class method to obtain the instance", UserWarning)
        self.__client_A_player = None
        self.__client_B_player = None
        self.__server_player = None
        self.__game = game
        # self.client_A_subsriber = rospy.Subscriber('/attacker_mouse_event', UInt8MultiArray, self.attacker_mouse_callback)
        # self.client_B_mouse_subsriber = rospy.Subscriber('/defender_mouse_event', UInt8MultiArray, self.defender_mouse_callback)

    @classmethod
    def get_instance():
        if Invoker.__instance == None:
            Invoker.__instance = Invoker()
        
        return Invoker.__instance

    def run_terminal(self):
        current_identity = Identity.ATTACK
        while (True):
            input_str = input()
            
            # signin A dctime
            # if (input_str == "signin"):
            #     if 



            Invoker.logger.info(f"Received Command \"{input_str}\" from terminal")

    # def attacker_mouse_callback(self, message):
    #     print("message")
    #     print(type(message))

    # def defender_mouse_callback(self, message):
    #     print("message")
    #     print(type(message))
