
"""
Social Media Platform (Text File Version)
-----------------------------------------

This is a simple command-line-based social media platform built using 
Object-Oriented Programming (OOP) concepts in Python. It allows users to:

1. Sign up by creating a username and password.
2. Log in using their credentials.
3. Create and view personal posts.

Features:
- User credentials are stored in a 'users.txt' file.
- Posts are stored in a 'posts.txt' file using 'username::post' format.
- Encapsulated logic using User and SocialMediaPlatform classes.
- Data persists between runs via basic text file storage.

This program is for educational purposes and does not include password hashing or 
robust security — it is ideal for learning file handling and OOP in Python.
"""

import os

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.posts = []

    def check_password(self, password):
        return self.password == password

    def add_post(self, post_content):
        self.posts.append(post_content)
        with open("posts.txt", "a") as f:
            f.write(f"{self.username}::{post_content}\n")

    def view_posts(self):
        print(f"\n--- {self.username}'s Posts ---")
        found = False
        if os.path.exists("posts.txt"):
            with open("posts.txt", "r") as f:
                for line in f:
                    uname, content = line.strip().split("::", 1)
                    if uname == self.username:
                        print(f"- {content}")
                        found = True
        if not found:
            print("No posts yet.")
        print("-----------------------------\n")


class SocialMediaPlatform:
    def __init__(self):
        self.users = {}  # username -> User instance
        self.load_users()

    def load_users(self):
        if not os.path.exists("users.txt"):
            # File doesn't exist; create it
            with open("users.txt", "w") as f:
                pass  # Just create an empty file
            print("Created new 'users.txt' file.")

        with open("users.txt", "r") as f:
            for line in f:
                if line.strip():  # Skip empty lines
                    username, password = line.strip().split(",", 1)
                    self.users[username] = User(username, password)

    def save_user(self, user):
        with open("users.txt", "a") as f:
            f.write(f"{user.username},{user.password}\n")

    def signup(self):
        username = input("Choose a username: ")
        if username in self.users:
            print("Username already exists! Try logging in.")
            return None
        password = input("Choose a password: ")
        user = User(username, password)
        self.users[username] = user
        self.save_user(user)
        print("Signup successful!")
        return user

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = self.users.get(username)
        if user and user.check_password(password):
            print("Login successful!")
            return user
        else:
            print("Invalid credentials!")
            return None

    def run(self):
        print("Welcome to File-Based Social!")
        while True:
            choice = input("Do you want to 'login' or 'signup'? (or type 'exit' to quit): ").strip().lower()
            if choice == 'signup':
                user = self.signup()
            elif choice == 'login':
                user = self.login()
            elif choice == 'exit':
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
                continue

            if user:
                while True:
                    action = input("What would you like to do? (post/view/logout): ").strip().lower()
                    if action == 'post':
                        content = input("Write your post: ")
                        user.add_post(content)
                        print("Post added!")
                    elif action == 'view':
                        user.view_posts()
                    elif action == 'logout':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid action.")


def main():
    platform = SocialMediaPlatform()
    platform.run()


if __name__ == "__main__":
    main()
