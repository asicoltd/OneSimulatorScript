# OneSimulatorScript
Automated report generator for ONE Simulator 1.4.1
Save the details2.py at one_1.4.1/ file


ONE Simulator Automation Tool
This tool automates running simulations with the ONE (Opportunistic Network Environment) Simulator by modifying configuration files, generating random values, and processing simulation reports. The tool provides a user-friendly interface via pyautogui to help users perform tasks like manual input, auto-generating simulation configurations, and modifying default settings.

Table of Contents
Requirements
Installation
Usage
Features
Manual Input Mode
Auto Generate Mode
Modify Settings Mode
Report Summary Mode
File Structure
FAQ
Requirements
Before running the script, ensure you have the following installed:

Python 3.6 or later
ONE Simulator (v1.4.1 or later)
pandas (pip install pandas)
pyautogui (pip install pyautogui)
pandasgui (pip install pandasgui)
Operating system: Windows (for running .bat scripts)
Installation
Clone the repository or download the script.

Ensure that the ONE simulator is installed and properly configured on your system.

Update the paths in the script where .bat files are referenced, if necessary (i.e., compile.bat, one.bat).

Install the necessary Python dependencies using pip:

bash
Copy code
pip install pandas pyautogui pandasgui
Ensure that your ONE simulator is installed in the correct directory and the .bat scripts (compile.bat, one.bat) are available.

Usage
Run the Python script to start the automation tool:

bash
Copy code
python one_simulator_automation.py
A GUI window will pop up with options:

Manual Input: Manually enter simulation parameters.
Auto Generate: Automatically generate simulation configurations with random parameters.
Modify Settings: Modify specific settings like transmit speed, range, or number of hosts.
Report Summary: View a summary of simulation reports and extract important metrics.
Exit: Close the tool.
Follow the on-screen prompts and input the required information as needed.

Features
Manual Input Mode
Allows you to manually enter values like Scenario.endTime and choose a router type (EpidemicRouter, SprayAndWaitRouter, ProphetRouter).
The script will modify the default_settings.txt file and update the Scenario.endTime and router values accordingly.
After changes, the ONE simulator will run based on the modified configurations.
Auto Generate Mode
Automatically generate a random Scenario.endTime and router type for multiple iterations.
This mode is useful for running batch simulations without manual input.
After each iteration, the default_settings.txt file is updated, and the simulation is executed.
Modify Settings Mode
Modify specific simulation settings like transmit speed, transmit range, or the number of hosts.
The settings are updated in the default_settings.txt file, and the simulator is rerun with the new configurations.
Report Summary Mode
This mode gathers all simulation report files and extracts important metrics:
Delivery Probability
Overhead Ratio
Latency
Response Probability
The extracted data is presented in a pandas DataFrame and can be viewed or exported as a CSV file.
File Structure
graphql
Copy code
├── one_simulator_automation.py   # Main script
├── default_settings.txt          # Settings file to be modified by the script
├── compile.bat                   # Batch file to compile ONE simulator
├── one.bat                       # Batch file to run ONE simulator
├── README.md                     # This README file
├── out.csv                       # Generated CSV from the report summary
└── reports/                      # ONE simulator report folder
FAQ
Q1. What happens if the default_settings.txt file is missing?

If the default_settings.txt file is not found, the script will terminate with a "File not found" error. Ensure that the file is available in the correct directory before running the tool.

Q2. What does the auto-generate feature do?

The auto-generate feature runs multiple simulations by automatically generating random values for Scenario.endTime and selecting random routers. You can specify how many iterations (loops) you want to run.

Q3. How do I view the simulation reports?

After running simulations, you can use the Report Summary Mode to gather and view the results. The tool extracts metrics from the reports and displays them in a table. The data is also saved in a CSV file (out.csv) for further analysis.

Q4. Can I modify simulation parameters other than the ones listed?

Currently, the tool allows modification of Transmit Speed, Transmit Range, and Number of Hosts. You can extend this functionality by updating the code to modify other parameters in the default_settings.txt file.
