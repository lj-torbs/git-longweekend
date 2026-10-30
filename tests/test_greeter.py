import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import greeter

assert greeter.greet("Ana").endswith("Ana!"), "greet should end with the name and !"
if hasattr(greeter, "farewell"):
    assert "Ana" in greeter.farewell("Ana"), "farewell should include the name"
print("tests passed")
