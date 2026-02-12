from difflib import get_close_matches

class ManagerAI:
    """
    An orchestrator that interprets user input to determine which 
    sub-application (Game or Tool) should be launched.
    """
    def __init__(self, available_apps):
        """
        An orchestrator that interprets user input to determine which 
        sub-application (Game or Tool) should be launched.
        Args:
            available_apps (list): A list of strings representing the keys of available applications.
        """
        self.apps = available_apps

        # Mapping intents to lists of descriptive keywords for fuzzy/exact matching
        self.keywords = {
            "tic tac toe": ["tictactoe", "ttt", "tic tac toe"],
            "connect four": ["connect4", "c4", "connect four"],
            "calculator": ["plus", "minus", "sum", "divide", "times"]
        }

    def get_intent(self, user_input):
        """
        Analyzes the user's message and returns the matching application key.
        Args:
            user_input (str): The raw input string from the user.
        Returns:
            str: The key of the detected app, or None if no match is found.
        """
        user_input = user_input.lower()
        
        # 1. STEP: Check if any keyword is directly PART of the sentence
        for intent, keys in self.keywords.items():
            for k in keys:
                if k in user_input:
                    return intent
        
        # 2. STEP: If no direct match, check individual words (Fuzzy Matching)
        words = user_input.split()
        all_keys = [k for keys in self.keywords.values() for k in keys]
        
        for word in words:
            # We only match words with a certain length to avoid false positives
            if len(word) < 3: continue 
            
            matches = get_close_matches(word, all_keys, n=1, cutoff=0.7)
            if matches:
                for intent, keys in self.keywords.items():
                    if matches[0] in keys:
                        return intent
                        
        return None