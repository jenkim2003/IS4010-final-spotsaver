import json
from datetime import datetime, timedelta
from pathlib import Path

# CHANGED: Store data in the same directory as this script so it is visible
DATA_FILE = Path(__file__).parent / "spotsaver_data.json"

class ParkingManager:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        # Ensure the file exists immediately upon starting
        if not self.data_file.exists():
            self._initialize_file()
        self.current_ticket = self._load_data()

    def _initialize_file(self):
        """Creates an empty JSON file so the user can see where data is stored."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump({}, f)
        except IOError as e:
            print(f"Error creating data file: {e}")

    def _load_data(self):
        """Loads the parking data from the JSON file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                # If the file contains an empty dictionary {}, return None
                if not data:
                    return None
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
        # CHANGED: Do not delete the file! Just empty the data inside it.
        # This keeps the file visible to the user.
        self._save_data()

    def _save_data(self):
        """Saves current ticket to file."""
        data_to_save = self.current_ticket if self.current_ticket else {}
        with open(self.data_file, 'w') as f:
            json.dump(data_to_save, f, indent=4)
