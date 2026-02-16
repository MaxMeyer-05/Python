import json
import os

class StatsManager:
    """
    Manages game records and provides dynamic answers to user queries.
    """
    def __init__(self, filepath="data/stats.json"):
        self.filepath = filepath
        self._initialize_storage()

    def _initialize_storage(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump({"user": 0, "ai": 0, "draw": 0}, f)

    def get_dynamic_answer(self, user_msg):
        """
        Filters the stats based on what the user specifically asked for.
        """
        with open(self.filepath, 'r') as f:
            data = json.load(f)

        msg = user_msg.lower()
        
        if "lose" in msg or "lost" in msg or "ai win" in msg:
            return f"You lost {data['ai']} times so far."
        elif "win" in msg or "won" in msg:
            return f"You have won {data['user']} times!"
        elif "draw" in msg or "tie" in msg:
            return f"There were {data['draw']} draws."
        
        # Default: show all stats
        return (f"Current Standings: \n"
                f"Your Wins: {data['user']} | AI Wins: {data['ai']} | Draws: {data['draw']}")

    def record_result(self, winner):
        """Saves a win/loss/draw."""
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        
        data[winner] += 1
        
        with open(self.filepath, 'w') as f:
            json.dump(data, f)