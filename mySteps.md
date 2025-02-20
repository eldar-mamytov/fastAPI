# fastAPI project steps

This document outlines the step-by-step process followed to build this project

# Steps

1) New repository in GitHub
    - Created a new repository "fastAPI.git"
    - Coppied the SSH URL 

2) Setting up SSH key for GitHub in my MacBook
    - Generate a new SSH key:
        bash: ssh-keygen -t ed25519 -C "eldarmmtv@gmail.com"
            # saves the key in the deafault location (~/.ssh/id_ed25519)
    - Adding the SSH key to the SSH agent:
        bash: eval "$(ssh-agent -s)"
        bash: ssh-add ~/.ssh/id_ed25519
    - Copying my public key:
        bash: cat ~/.ssh/id_ed25519.pub
            # ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFVVGAaUySQD/QdmE4VUHUZCVYuxAKGQ6T04U2+V6+3f eldarmmtv@gmail.com
    - Creating New SSH key in GitHub:
        go to Settings > SSH and GPG keys > New SSH Key
        paste the copied ey and save it
    - Testing the connection:
        bash: ssh -T git@github.com
            # Hi eldar-mamytov! You've successfully authenticated, but GitHub does not provide shell access.

3) Creating a project
    - Creating a project directory:
        bash: mkdir ~/Desktop/fastAPI_projects/github-aws-fastapi-2
        bash: cd ~/Desktop/fastAPI_projects/github-aws-fastapi-2
    - Initializing a git repository:
        bash: git init
    - Adding the remote repository:
        bash: git remote add origin git@github.com:eldar-mamytov/fastAPI.git
    - Verifying if the remote repository was added:
        bash: git remote -v
            # origin	git@github.com:eldar-mamytov/fastAPI.git (fetch)
            # origin	git@github.com:eldar-mamytov/fastAPI.git (push)

4) Setting up a virtual environment
    - Creating a virtual environemnt:
        bash: python3 -m venv venv
    - Activating it:
        bash: source venv/bin/activate
    - Installing FastAPI and Uvicorn:
        bash: pip install fastapi uvicorn

