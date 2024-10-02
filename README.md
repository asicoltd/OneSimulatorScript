<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>ONE Simulator Automation Tool</h1>

<p>This tool automates running simulations with the ONE (Opportunistic Network Environment) Simulator by modifying configuration files, generating random values, and processing simulation reports. The tool provides a user-friendly interface via <code>pyautogui</code> to help users perform tasks like manual input, auto-generating simulation configurations, and modifying default settings.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#file-structure">File Structure</a></li>
    <li><a href="#faq">FAQ</a></li>
</ul>

<h2 id="requirements">Requirements</h2>
<p>Before running the script, ensure you have the following installed:</p>
<ul>
    <li>Python 3.6 or later</li>
    <li>ONE Simulator (v1.4.1 or later)</li>
    <li><code>pandas</code> (<code>pip install pandas</code>)</li>
    <li><code>pyautogui</code> (<code>pip install pyautogui</code>)</li>
    <li><code>pandasgui</code> (<code>pip install pandasgui</code>)</li>
    <li>Operating system: Windows (for running <code>.bat</code> scripts)</li>
</ul>

<h2 id="installation">Installation</h2>
<ol>
    <li>Clone the repository or download the script.</li>
    <li>Ensure that the ONE simulator is installed and properly configured on your system.</li>
    <li>Update the paths in the script where <code>.bat</code> files are referenced, if necessary (i.e., <code>compile.bat</code>, <code>one.bat</code>).</li>
    <li>Install the necessary Python dependencies using pip:
        <pre><code>pip install pandas pyautogui pandasgui</code></pre>
    </li>
    <li>Ensure that your ONE simulator is installed in the correct directory and the <code>.bat</code> scripts (<code>compile.bat</code>, <code>one.bat</code>) are available.</li>
</ol>

<h2 id="usage">Usage</h2>
<ol>
    <li>Run the Python script to start the automation tool:
        <pre><code>details2.py</code></pre>
    </li>
    <li>A GUI window will pop up with options:
        <ul>
            <li><strong>Manual Input</strong>: Manually enter simulation parameters.</li>
            <li><strong>Auto Generate</strong>: Automatically generate simulation configurations with random parameters.</li>
            <li><strong>Modify Settings</strong>: Modify specific settings like transmit speed, range, or number of hosts.</li>
            <li><strong>Report Summary</strong>: View a summary of simulation reports and extract important metrics.</li>
            <li><strong>Exit</strong>: Close the tool.</li>
        </ul>
    </li>
    <li>Follow the on-screen prompts and input the required information as needed.</li>
</ol>

<h2 id="features">Features</h2>

<h3 id="manual-input-mode">Manual Input Mode</h3>
<p>Allows you to manually enter values like <code>Scenario.endTime</code> and choose a router type (EpidemicRouter, SprayAndWaitRouter, ProphetRouter). The script will modify the <code>default_settings.txt</code> file and update the <code>Scenario.endTime</code> and router values accordingly. After changes, the ONE simulator will run based on the modified configurations.</p>

<h3 id="auto-generate-mode">Auto Generate Mode</h3>
<p>Automatically generate a random <code>Scenario.endTime</code> and router type for multiple iterations. This mode is useful for running batch simulations without manual input. After each iteration, the <code>default_settings.txt</code> file is updated, and the simulation is executed.</p>

<h3 id="modify-settings-mode">Modify Settings Mode</h3>
<p>Modify specific simulation settings like transmit speed, transmit range, or the number of hosts. The settings are updated in the <code>default_settings.txt</code> file, and the simulator is rerun with the new configurations.</p>

<h3 id="report-summary-mode">Report Summary Mode</h3>
<p>This mode gathers all simulation report files and extracts important metrics:</p>
<ul>
    <li>Delivery Probability</li>
    <li>Overhead Ratio</li>
    <li>Latency</li>
    <li>Response Probability</li>
</ul>
<p>The extracted data is presented in a pandas DataFrame and can be viewed or exported as a CSV file.</p>

<h2 id="file-structure">File Structure</h2>
<pre>
<code>
├── one_simulator_automation.py   # Main script
├── default_settings.txt          # Settings file to be modified by the script
├── compile.bat                   # Batch file to compile ONE simulator
├── one.bat                       # Batch file to run ONE simulator
├── README.md                     # This README file
├── out.csv                       # Generated CSV from the report summary
└── reports/                      # ONE simulator report folder
</code>
</pre>

<h2 id="faq">FAQ</h2>

<h3>Q1. What happens if the <code>default_settings.txt</code> file is missing?</h3>
<p>If the <code>default_settings.txt</code> file is not found, the script will terminate with a "File not found" error. Ensure that the file is available in the correct directory before running the tool.</p>

<h3>Q2. What does the <strong>auto-generate</strong> feature do?</h3>
<p>The auto-generate feature runs multiple simulations by automatically generating random values for <code>Scenario.endTime</code> and selecting random routers. You can specify how many iterations (loops) you want to run.</p>

<h3>Q3. How do I view the simulation reports?</h3>
<p>After running simulations, you can use the <strong>Report Summary Mode</strong> to gather and view the results. The tool extracts metrics from the reports and displays them in a table. The data is also saved in a CSV file (<code>out.csv</code>) for further analysis.</p>

<h3>Q4. Can I modify simulation parameters other than the ones listed?</h3>
<p>Currently, the tool allows modification of <strong>Transmit Speed</strong>, <strong>Transmit Range</strong>, and <strong>Number of Hosts</strong>. You can extend this functionality by updating the code to modify other parameters in the <code>default_settings.txt</code> file.</p>

</body>
</html>
