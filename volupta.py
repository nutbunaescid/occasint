# Import necessary libraries
import os
import subprocess

# Define a function to create a new repository
def create_repository(repo_name):
    """
    Create a new local git repository with the specified name.

    Parameters:
    repo_name (str): The name of the repository to create.
    """
    try:
        # Check if the repository already exists
        if not os.path.exists(repo_name):
            # Create a new directory for the repository
            os.makedirs(repo_name)
            # Change the current working directory to the new repository
            os.chdir(repo_name)
            # Initialize the repository
            subprocess.run(['git', 'init'], check=True)
            print(f"Repository '{repo_name}' successfully created.")
        else:
            print(f"Error: Repository '{repo_name}' already exists.")
    except Exception as e:
        print(f"An error occurred while creating the repository: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'my_new_repo' with the desired repository name
    create_repository('my_new_repo')
