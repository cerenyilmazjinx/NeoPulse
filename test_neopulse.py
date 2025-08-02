# test_neopulse.py
"""
Tests for NeoPulse module.
"""

import unittest
from neopulse import NeoPulse

class TestNeoPulse(unittest.TestCase):
    """Test cases for NeoPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeoPulse()
        self.assertIsInstance(instance, NeoPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeoPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
