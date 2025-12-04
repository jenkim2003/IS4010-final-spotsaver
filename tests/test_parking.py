import pytest
import sys
import os
from pathlib import Path

# This logic adds the 'src' folder to Python's list of places to look for code
# so we can import our parking_manager.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from parking_manager import ParkingManager

# We use a fake file for testing so we don't overwrite your real parking spot
TEST_DB_FILE = Path("test_parking_data.json")

@pytest.fixture
def manager():
    """
    This is a 'fixture'. It runs before every test to give us a fresh
    ParkingManager linked to a temporary test file.
    """
    # Create manager with test file
    pm = ParkingManager(data_file=TEST_DB_FILE)
    yield pm
    # Cleanup: Delete the test file after the test finishes
    if TEST_DB_FILE.exists():
        TEST_DB_FILE.unlink()

def test_park_creates_file(manager):
    """Test that parking a car actually creates the data file."""
    manager.park_car("Test Level 1", 2)
    assert TEST_DB_FILE.exists()

def test_park_stores_correct_data(manager):
    """Test that the location and time are saved correctly."""
    ticket = manager.park_car("Gym Lot", 1, 30)
    assert ticket["location"] == "Gym Lot"
    assert ticket["duration_minutes"] == 90 # 1 hour + 30 mins

def test_clear_removes_file(manager):
    """Test that clearing the parking deletes the file."""
    manager.park_car("Test Spot", 1)
    manager.clear_parking()
    assert not TEST_DB_FILE.exists()
    assert manager.current_ticket is None

def test_status_message(manager):
    """Test that status returns a string."""
    manager.park_car("Test Spot", 1)
    status = manager.get_status()
    assert isinstance(status, str)
    assert "h" in status or "m" in status