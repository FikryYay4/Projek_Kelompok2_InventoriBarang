import os
import shutil
import inventory
import auth
import file_handler as fh

# Clean up previous test data if exists
if os.path.exists("data"):
    shutil.rmtree("data")

print("Debugging Test Start...")

# 1. Test File Handler
print("\n[Test] File Handler")
test_data = [{"id": 1, "name": "Test"}]
fh.save_data("test.json", test_data)
loaded_data = fh.load_data("test.json")
if loaded_data == test_data:
    print("PASS: Save and Load Data")
else:
    print("FAIL: Save and Load Data")

# 2. Test Auto ID Logic
print("\n[Test] Auto ID Logic")
# Case 1: Empty list
id1 = inventory.generate_id([])
if id1 == "BRG-001":
    print(f"PASS: First ID is {id1}")
else:
    print(f"FAIL: First ID is {id1}")

# Case 2: Existing items
items = [{"id": "BRG-001"}, {"id": "BRG-005"}]
id2 = inventory.generate_id(items)
if id2 == "BRG-006":
    print(f"PASS: Next ID after BRG-005 is {id2}")
else:
    print(f"FAIL: Next ID after BRG-005 is {id2}")

print("\nDebugging Test Complete.")
