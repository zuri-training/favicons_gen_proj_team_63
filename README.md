# Favigen Project

<!-- ABOUT THE PROJECT -->
## About The Project

This repository contains the codebase and project files of Project Favicon by Team 63 of the Zuri project phase.

### Technologies Used

The list of all the major technologies used in the project.

- [Django](https://www.djangoproject.com/)
- [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [CSS](https://web.dev/learn/css/)
- [Postgres](https://www.postgresql.org/)

<!-- CONTRIBUTING -->
## Contribution Guide

Please ensure your codes and changes are properly tested.

### Fork the Project Repo

Fork this repository to get a personal copy on your github account

### Clone the Repo to your local machine using

To clone the forked repository to your local machine, copy the URL for the forked repo, open command prompt and run:

`git clone <url-for-your-forked-repo>`

### Set Upstream Remote

Set your upstream remote so you can pull changes from upstream to update your repo by running:

`git remote add upstream https://github.com/zuri-training/favicons_gen_proj_team_63`

### Creating Feature Branch

First create a dev branch by running:

`git checkout -b dev`

Then make sure you're in the dev branch by running:

`git checkout dev`

Then create the feature branch (the branch you will be pushing you work to) by running:

`git checkout -b feature`

NB: For consistency, I would recommend we all use the above naming scheme and make sure to create any new branch from the dev branch and not main branch. Ensure your local dev branch is up to date with upstream remote dev branch before creating new branch.

### Set up Development Environment

Tip: Check the Getting Started guide below

### Making Changes

Make all your changes on your feature branch, add and commit your changes using a concise descriptive commit message

### Pulling Updates from Remote

Pull latest updates from Upstream branch by running:

`git pull upstream dev`

NB: If conflicts are encountered after pulling changes, please resolve them locally first before committing

### Pushing Changes

Publish your Feature Branch and changes to origin by running:

`git push origin active`

### Pull Request

Go to Github, open a Pull Request to the Upstream Remote dev branch and request a review by tagging team members

NB: Add a proper description of the changes made when making a Pull Request for easy review.

## Getting Started

Setup virtual environment:

1. Go to your project folder in your code editor (you should have cloned the project by now from the steps above)
2. Make sure in your terminal that you are in the root folder of the project
3. Create a virtual environment with `virtualenv venv`
4. Then activate the virtual environment with `source venv/scripts/activate`
5. Make sure `venv` appears on the left side of your terminal to confirm that it has activted
6. Install the project dependencies with `pip install -r requirements.txt`. This will install Django and any other package for this project
7. Now your VS Code color-coding should adjust since you have installed all the packages

Setup Postgres:

1. Go to [Postgres website](https://www.postgresql.org/download/) and download the latest Postgres version for your OS
2. Run the installer make sure all options are ticked including pgAdmin 4
3. In the Password section, enter a password you will be using for your Postgres and take note of this password as you will be using it very often
4. In the Port section, leave the default port as 5432, don't change it
5. Click next until it starts installing
6. At the end of the install, uncheck __Stack Builder__ and click finish
7. Open pgAdmin 4, when it loads, you will be asked to create master password. You can use the same password you used in Step 3, then click OK
8. Then on the left side panel, click on __Servers__ and you will be asked for you password from Step 3. Enter it and also tick __Save Password__  and click OK.
9. Then, still on the left side panel, right-click on __Databases__  and create a new database
10. The database name should be `ZuriconDB`, enter it then click OK
11. Now go to the project folder in your code editor (i.e. VS Code)
12. Create a `.env` file at the project root.
13. Populate your `.env` with the following:

    ```python
        DB_NAME=ZuriconDB
        USER=postgres
        PASSWORD=your postgres password
        HOST=localhost
        PORT=5432
        SECRET_KEY=your django secret key
        DEBUG=True
    ```

14. Now you can go to your code editor and run `python manage.py makemigrations`
15. Then after that run `python manage.py migrate`
16. You should not get any errors when you run `python manage.py runserver`. If you do, pls ask any of the other devs

NB:

- It is highly advisable to use Git Bash as your terminal app as it easily shows the current branch you're working in
- Team members should please ask questions if anything is not clear!
