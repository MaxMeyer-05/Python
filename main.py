from AI.manager_ai import ManagerAI
from AI.math_ai import MathAI
from Games.engine import play_loop
from Games.tictactoe import TicTacToe
from Games.connectFour import ConnectFour

def main():
    """
    Main entry point of the application. 
    Handles the high-level routing using a command-dispatch dictionary.
    """
    math_ai = MathAI()
    
    # Dispatcher dictionary using lambdas to delay execution until called
    # msg is passed so the calculator can extract the numbers from it
    apps = {
        "tic tac toe": lambda msg: play_loop(TicTacToe(), 9),
        "connect four": lambda msg: play_loop(ConnectFour(), 5),
        "calculator": lambda msg: print(f"\n[AI]: {math_ai.solve(msg)}")
    }

    manager = ManagerAI(list(apps.keys()))

    print("\n[AI]: Hello! I'm ready to help you. What would you like to do?")
    
    while True:
        user_msg = input("\nYou: ")
        if user_msg.lower() in ["exit", "ende", "bye"]: break

        # Determine what the user wants to do based on their message
        intent = manager.get_intent(user_msg)

        if intent in apps:
            apps[intent](user_msg)
        else:
            print("\n[AI]: I don't understand. Do you want to play a game or do some math?")

if __name__ == "__main__":
    main()