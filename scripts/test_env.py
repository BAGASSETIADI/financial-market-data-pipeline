from dotenv import load_dotenv
import os

load_dotenv()

print("PROJECT_ID:")
print(os.getenv("PROJECT_ID"))

print()

print("DATASET_ID:")
print(os.getenv("DATASET_ID"))