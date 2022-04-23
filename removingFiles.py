
import os
import shutil
import time

def main():

	deleted_files_count = 0
	path = r"C:\Users\rajat\Downloads\test C-99"
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for root_folder, dir, files in os.walk(path):

				for file in files:
					file_path = os.path.join(root_folder, file)

		
					if seconds >= get_file_or_folder_age(file_path):

						remove_file(file_path)
						deleted_files_count += 1
		else:
			if seconds >= get_file_or_folder_age(path):
				remove_file(path)
				deleted_files_count += 1 

	else:

		print(f'"{path}" is not found')
	print(f"Total files deleted: {deleted_files_count}")

def remove_file(path):
	if not os.remove(path):

		print(f"{path} is removed successfully")

	else:

		print("Unable to delete the "+path)


def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime


if __name__ == '__main__':
	main()
