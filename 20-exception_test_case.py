def write_test_file():
    with open("test2.txt", 'w') as file:
        file.write('test')
        file.write('its a game \t 50\n')
        file.write('time splis away\t590')

def safe_file_read(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"⚠️ File '{filepath}' not found.")
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
    return []

# Write to the file
write_test_file()

# Read from the correct file
data = safe_file_read("test2.txt")
print("✅ File content:")
print(data)

# Try to read a non-existent file
print("\n🔍 Trying to read non-existent file...")
_ = safe_file_read("test.txte")
