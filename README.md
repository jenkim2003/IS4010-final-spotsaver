# SpotSaver CLI: IS4010 Final Project

SpotSaver is a command-line tool that helps you track where you parked and more importantly when your meter expires. As a student, parking on campus can be a nightmare; this tool ensures you never lose your car or get a ticket again.

**Features:**

Park: Save your location and meter duration.

Status: See exactly how much time is left (e.g., "1h 15m").

Alerts: Visually distinct warnings when your meter is EXPIRED.

Persistence: Remembers your spot even if you restart your computer.

**Installation:**
Clone the repository: git clone [cd IS4010-final-spotsaver](https://github.com/jenkim2003/IS4010-final-spotsaver)

Install dependencies: pip install -r requirements.txt

**Usage:**
1. Park your car: python src/main.py park --loc "Campus Garage B, Level 3" --hours 2 --mins 30

2. Check status: python src/main.py status

3. Clear session: python src/main.py clear

**Testing:**
Run the automated test suite: pytest

**AI Assistance:**
This project was developed with the assistance of Gemini for logic verification and CI/CD setup. See for details.

**Contact:**

**Mariah Jenkins** (jenkim2003) Project Link: https://github.com/jenkim2003/IS4010-final-spotsaver