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
        """
        self.apps = available_apps

        # Mapping intents to lists of descriptive keywords for fuzzy/exact matching
        self.keywords = {
            "tic tac toe": ["tictactoe", "ttt", "tic tac toe", "play"],
            "connect four": ["vier gewinnt", "connect4", "c4", "viererreihe"],
            "calculator": ["calculate", "math", "plus", "minus", "summe"]
        }

    def get_intent(self, user_input):
        """
        Analyzes the user's message and returns the matching application key.
        
        Returns:
            str: The key of the detected app, or None if no match is found.
        """
        user_input = user_input.lower()
        
        # 1. Exact keyword matching
        for app_name, synonyms in self.keywords.items():
            if any(s in user_input for s in synonyms):
                return app_name
        
        # 2. Fuzzy matching to handle typos (e.g. "TiktakTo")
        all_synonyms = [s for syn_list in self.keywords.values() for s in syn_list]
        words = user_input.split()
        for word in words:
            match = get_close_matches(word, all_synonyms, n=1, cutoff=0.6)
            if match:
                # Find which intent the matched keyword belongs to
                for app_name, synonyms in self.keywords.items():
                    if match[0] in synonyms:
                        return app_name
        
        return None