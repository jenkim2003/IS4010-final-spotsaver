AI Agents Usage Log

**Tools Used:**
Gemini (Google): Used as the primary coding partner for project structure, logic implementation, and debugging.

**GitHub Actions** Used for automated testing.

**Development Process**

Ideation: Gemini suggested 3 project ideas. I selected the Parking Tracker ("SpotSaver") because as a student, I relate to campus parking struggles. I often lose track of time or forget where I parked, so this tool solves a real personal problem while fitting the project complexity requirements.

Structure: The project follows a professional Python layout with src/ and tests/ directories.

**Implementation:**

Created parking_manager.py for backend logic (JSON storage, datetime math).

Created main.py using argparse and rich for the CLI interface.

Testing: Wrote pytest scripts to verify file creation and time calculations.

CI/CD: Configured .github/workflows/tests.yml to run tests on every push.

**Sample Prompts:**
"Generate a Python CLI structure for a parking tracker app that saves data to a JSON file."

"How do I calculate the difference between the current time and a future timestamp in Python?"

"Create a GitHub Actions workflow that runs pytest every time I push code."


**Reflection:**
Using AI helped verify the logic for datetime calculations, which can be tricky. It also helped generate the correct YAML structure for GitHub Actions.