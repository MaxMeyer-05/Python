import re

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

        # Define keywords for each app to help with intent recognition
        self.keywords = {
            "stats": {
                "strong_markers": ["win", "lose", "score", "record", "stats", "draw", "tie"],
                "soft_markers": ["how", "many", "times", "total", "number", "did", "i"],
                "priority": 3  # Highest priority
            },
            "calculator": {
                "strong_markers": ["plus", "minus", "times", "divided", "calculate", "sum", "root"],
                "soft_markers": ["is", "what", "total", "result", "number"],
                "priority": 1  # Lower priority for general questions
            },
            "tic tac toe": {
                "strong_markers": ["ttt", "tic", "tac", "toe"],
                "soft_markers": ["play", "game", "start"],
                "priority": 2
            },
            "connect four": {
                "strong_markers": ["c4", "connect", "four", "vier", "gewinnt"],
                "soft_markers": ["play", "game", "start"],
                "priority": 2
            }
        }

    def get_intent(self, user_input):
        """
        Analyzes the user's message and returns the matching application key.
        Args:
            user_input (str): The raw input string from the user.
        Returns:
            str: The key of the detected app, or None if no match is found.
        """
        msg = user_input.lower()
        words = re.sub(r'[^a-z0-9\s]', '', msg).split()

        scores = {intent: 0 for intent in self.keywords}
        
        # 1. STEP: Check for strong and soft markers in the message
        for intent, data in self.keywords.items():
            for word in words:
                if word in data["strong_markers"]:
                    scores[intent] += 10 * data["priority"]
                if word in data["soft_markers"]:
                    scores[intent] += 1 * data["priority"]
        
        # 2. STEP: Apply some hard rules for edge cases (e.g., if "win" is mentioned, it's likely about stats)
        if any(w in words for w in self.keywords["stats"]["strong_markers"]):
            scores["calculator"] = 0
            scores["stats"] += 20                        
        
        best_intent = max(scores, key=scores.get)
        return best_intent if scores[best_intent] > 0 else None