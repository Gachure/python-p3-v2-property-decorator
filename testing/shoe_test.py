import sys
import os

# Add the lib directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib')))

from shoe import Shoe

def test_shoe_initialization():
    shoe = Shoe("Nike", 42, "Black")
    assert shoe.brand == "Nike"
    assert shoe.size == 42
    assert shoe.color == "Black"

def test_shoe_str():
    shoe = Shoe("Nike", 42, "Black")
    assert str(shoe) == "Nike shoes, Size 42, Color Black"
