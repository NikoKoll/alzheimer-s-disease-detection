# alzheimer-s-disease-detection
Alzheimer's disease detection using deep learning

## Setting Up a Virtual Environment and Running an app.py File

Introduction:

This guide provides step-by-step instructions for creating a virtual environment (venv) and running an app.py file on different operating systems: Windows, MacOS, and Linux. Using a virtual environment ensures that your Python project dependencies are isolated and don't conflict with other projects.

Prerequisites:

Before proceeding, ensure that you have the following:

Python installed on your system. You can download it from Python's official website.
Basic knowledge of navigating the command line interface (CLI) on your respective operating system.
Step 1: Cloning the Repository

If you haven't already, clone or download the repository containing the app.py file to your local machine.

bash
Αντιγραφή κώδικα
git clone <repository_url>

Unzip the models folder and copy the .h5 file to a new "models" folder inside your project

Step 2: Creating a Virtual Environment

Windows:

Open Command Prompt or PowerShell and navigate to the project directory.

bash
Αντιγραφή κώδικα
cd path/to/project
Create a virtual environment named venv.

bash
Αντιγραφή κώδικα
python -m venv venv
Activate the virtual environment.

bash
Αντιγραφή κώδικα
venv\Scripts\activate
MacOS and Linux:

Open Terminal and navigate to the project directory.

bash
Αντιγραφή κώδικα
cd path/to/project
Create a virtual environment named venv.

bash
Αντιγραφή κώδικα
python3 -m venv venv
Activate the virtual environment.

bash
Αντιγραφή κώδικα
source venv/bin/activate
Step 3: Installing Dependencies

Ensure that you're in the virtual environment.

Install the project dependencies using pip.

bash
Αντιγραφή κώδικα
pip install -r requirements.txt
Step 4: Running the Application

Run the app.py file using Python.

bash
Αντιγραφή κώδικα
python app.py
