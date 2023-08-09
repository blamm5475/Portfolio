import os
import shutil

def main():
    source_dir = os.getcwd()
    destination_dir = input("Enter the destination directory: ")

    if not os.path.exists(destination_dir):
        print("Destination directory does not exist.")
        return

    prefix = input("Enter the first 4 characters to filter files: ")

    for filename in os.listdir(source_dir):
        if filename.startswith(prefix):
            source_path = os.path.join(source_dir, filename)
            destination_path = os.path.join(destination_dir, filename)

            try:
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {destination_dir}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    main()