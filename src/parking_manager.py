import json
from datetime import datetime, timedelta
from pathlib import Path

# This helps us store data in a hidden file in the user's home directory
DATA_FILE = Path.home() / ".spotsaver_data.json"

class ParkingManager:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.current_ticket = self._load_data()

    def _load_data(self):
        """Loads the parking data from the JSON file."""
        if not self.data_file.exists():
            return None
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return data
        except (json.JSONDecodeError, IOError):
            return None

    def park_car(self, location, hours, minutes=0):
        """Starts a new parking session."""
        start_time = datetime.now()
        duration = timedelta(hours=hours, minutes=minutes)
        end_time = start_time + duration

        self.current_ticket = {
            "location": location,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration_minutes": (hours * 60) + minutes
        }
        self._save_data()
        return self.current_ticket

    def get_status(self):
        """Calculates time remaining."""
        if not self.current_ticket:
            return "No active parking session."

        end_time = datetime.fromisoformat(self.current_ticket["end_time"])
        now = datetime.now()
        
        remaining = end_time - now
        
        if remaining.total_seconds() <= 0:
            return "EXPIRED"
        
        # Return pretty string: "1h 30m"
        total_seconds = int(remaining.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours}h {minutes}m"

    def clear_parking(self):
        """Deletes the current parking session."""
        self.current_ticket = None
        if self.data_file.exists():
            self.data_file.unlink() # Deletes the file

    def _save_data(self):
        """Saves current ticket to file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.current_ticket, f, indent=4)