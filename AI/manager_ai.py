from difflib import get_close_matches

class ManagerAI:
    def __init__(self, available_apps):
        self.apps = available_apps
        self.keywords = {
            "tic tac toe": ["tictactoe", "ttt", "tic tac toe", "play"],
            "connect four": ["vier gewinnt", "connect4", "c4", "viererreihe"],
            "calculator": ["calculate", "math", "plus", "minus", "summe"]
        }

    def get_intent(self, user_input):
        user_input = user_input.lower()
        
        for app_name, synonyms in self.keywords.items():
            if any(s in user_input for s in synonyms):
                return app_name
        
        all_synonyms = [s for syn_list in self.keywords.values() for s in syn_list]
        words = user_input.split()
        for word in words:
            match = get_close_matches(word, all_synonyms, n=1, cutoff=0.6)
            if match:
                for app_name, synonyms in self.keywords.items():
                    if match[0] in synonyms:
                        return app_name
        
        return None