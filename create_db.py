import os
import sys

from app.database import create_database


def main():
	# Ensure the database directory exists (sqlite won't create directories)
	db_dir = os.path.join(os.path.dirname(__file__), "database")
	os.makedirs(db_dir, exist_ok=True)

	try:
		create_database()
	except Exception as e:
		print(f"Failed to create database: {e}")
		sys.exit(1)

	print("Database created successfully")


if __name__ == "__main__":
	main()