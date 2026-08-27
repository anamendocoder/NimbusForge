# test_nimbusforge.py
"""
Tests for NimbusForge module.
"""

import unittest
from nimbusforge import NimbusForge

class TestNimbusForge(unittest.TestCase):
    """Test cases for NimbusForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NimbusForge()
        self.assertIsInstance(instance, NimbusForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NimbusForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
