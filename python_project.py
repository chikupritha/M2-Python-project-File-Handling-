
import os
import shutil

# Dictionary to map file extensions to their respective folders
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.odt'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.ogg'],
    'Spreadsheets': ['.xls', '.xlsx', '.ods'],
    'Presentations': ['.ppt', '.pptx', '.odp']
}

def organize_files(directory):
    # Create folders for each file type if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Skip folders
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Move the file to its corresponding folder
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                break

def create_custom_folder(directory):
    folder_name = input("Enter the name of the folder you want to create: ").strip()
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created successfully!")
    else:
        print(f"Folder '{folder_name}' already exists.")


def delete_folder(directory):
    """
    Deletes a specified folder in the given directory after confirmation.
    """
    folder_name = input("Enter the name of the folder you want to delete: ").strip()
    folder_path = os.path.join(directory, folder_name)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        confirm = input(f"Are you sure you want to delete the folder '{folder_name}'? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                shutil.rmtree(folder_path)
                print(f"Folder '{folder_name}' deleted successfully!")
            except Exception as e:
                print(f"Error deleting folder '{folder_name}': {e}")
        else:
            print("Folder deletion canceled.")
    else:
        print(f"The folder '{folder_name}' does not exist in the specified directory.")


def menu():
    while True:
        print("\n--- File Organizer Menu ---")
        print("1. Organize files")
        print("2. Create a custom folder")
        print("3. Delete folder name")
        print("4. Change directory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            directory = input("Enter the directory path to organize: ").strip()
            if os.path.exists(directory) and os.path.isdir(directory):
                organize_files(directory)
                print("Files organized successfully!")
            else:
                print("The specified directory does not exist or is invalid.")

        elif choice == '2':
            directory = input("Enter the directory where you want to create a folder: ").strip()
            if os.path.exists(directory) and os.path.isdir(directory):
                create_custom_folder(directory)
            else:
                print("The specified directory does not exist or is invalid.")

        elif choice == '3':
            directory = input("Enter the directory containing the folder you want to delete: ").strip()
            if os.path.exists(directory) and os.path.isdir(directory):
                delete_folder(directory)
            else:
                print("The specified directory does not exist or is invalid.")

        elif choice == '4':
            directory = input("Enter the new directory path: ").strip()
            if os.path.exists(directory) and os.path.isdir(directory):
                print(f"Changed directory to: {directory}")
            else:
                print("The specified directory does not exist or is invalid.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the menu
menu()
