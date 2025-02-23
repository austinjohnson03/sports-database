import os 

def create_path(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created file path: {dir_path}")

