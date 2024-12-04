import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import json
repo_mapping = {
    0: "microsoft/vscode",
    1: "facebook/react",
    2: "tensorflow/tensorflow",
    3: "vuejs/vue",
    4: "airbnb/javascript",
    5: "torvalds/linux",
    6: "laravel/laravel",
    7: "flutter/flutter",
    8: "nodejs/node",
    9: "apache/incubator-dubbo"
}
GITHUB_API_BASE_URL = "https://api.github.com/repos/"
def get_github_repo_info(repo_name, last_digit):
    """Fetches and processes the JSON data for a given GitHub repository."""
    try:
        repo_url = get_repo_url_from_last_digit(last_digit, repo_name)
        if repo_url is None:
            return f"Repository not found for last digit {last_digit} and name {repo_name}"
        response = requests.get(repo_url)
        response.raise_for_status()
        data = response.json()
        repo_info = {
            'company': data.get('owner', {}).get('login', None), #Company is often under owner.login
            'created_at': data.get('created_at', None),
            'email': None, #Usually not directly available in public API
            'id': data.get('id', None),
            'name': data.get('name', None),
            'url': data.get('html_url', None)
        }
        return repo_info
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    except KeyError as e:
        return f"Error parsing JSON response: Missing key {e}"
def write_to_file(repo_info, filename="github_repo_info.json"):
    """Writes the repository information to a JSON file."""
    try:
        with open(filename, 'w') as outfile:
            json.dump(repo_info, outfile, indent=4)
        print(f"Data written to '{filename}'")
    except Exception as e:
        print(f"Error writing to file: {e}")
def process_repo():
    """Handles button click, gets repo data, and writes to file."""
    repo_name = repo_entry.get()
    last_digit_str = last_digit_entry.get()
    try:
        last_digit = int(last_digit_str)
        if not 0 <= last_digit <= 9:
            raise ValueError("Last digit must be between 0 and 9")
        repo_data = get_github_repo_info(repo_name, last_digit)
        write_to_file(repo_data)
        messagebox.showinfo("Success", "Repository data written to file.")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
def get_repo_url_from_last_digit(last_digit, repo_name):
    """Constructs the GitHub API URL based on the last digit and repo name."""
    repo_full_name = repo_mapping.get(last_digit)
    if repo_full_name is not None and repo_full_name.lower() == repo_name.lower(): #case-insensitive matching
      return GITHUB_API_BASE_URL + repo_full_name
    else:
      return None
root = tk.Tk()
root.title("GitHub Repo Info")
root.mainloop()