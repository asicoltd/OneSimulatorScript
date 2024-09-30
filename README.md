<h2>ONE Simulator Automation Script</h2>

<p>This Python script automates tasks related to the ONE Simulator, allowing users to manually input settings, auto-generate configurations, modify simulation settings and generate summary reports using a graphical interface with <code>pyautogui</code>.</p>

<h3>Key Components</h3>

<h4>1. Options Function (<code>options()</code>)</h4>
<ul>
  <li>Presents a GUI using <code>pyautogui.confirm()</code> with options such as "Manual Input", "Auto Generate", "Modify Settings", "Report Summary", and "Exit".</li>
  <li>Maps each user selection to a specific task in the program, directing the flow of the script based on user input.</li>
</ul>

<h4>2. Batch File Execution</h4>
<ul>
  <li>The script uses <code>subprocess.run()</code> to execute batch files like <code>compile.bat</code> and <code>one.bat -b 1</code>, automating tasks such as compiling and running the ONE simulator.</li>
</ul>

<h4>3. Manual Input Mode</h4>
<ul>
  <li>Allows the user to manually update specific settings in the <code>default_settings.txt</code> file, such as <code>Scenario.endTime</code> and the selected router type (e.g., <code>EpidemicRouter</code>, <code>SprayAndWaitRouter</code>, <code>ProphetRouter</code>).</li>
  <li>After the settings are modified, the script re-runs the simulator by executing a batch file.</li>
</ul>

<h4>4. Auto Generate Mode</h4>
<ul>
  <li>Automatically generates random values for <code>Scenario.endTime</code> and selects either a random or user-specified router.</li>
  <li>Updates the <code>default_settings.txt</code> file and runs multiple simulations based on the number of loops specified by the user.</li>
</ul>

<h4>5. Modify Settings Mode</h4>
<ul>
  <li>Allows the user to modify simulation settings like "Transmit Speed", "Transmit Range", and "Number of Hosts" directly in the <code>default_settings.txt</code> file.</li>
  <li>The changes are saved and the simulator is re-run after the modifications.</li>
</ul>

<h4>6. Report Summary Mode</h4>
<ul>
  <li>Fetches the simulation reports stored in a specific folder (e.g., <code>../one_1.4.1/reports</code>).</li>
  <li>Extracts and displays important metrics like:
    <ul>
      <li><code>delivery_prob</code> (Delivery Probability)</li>
      <li><code>overhead_ratio</code> (Overhead Ratio)</li>
      <li><code>latency_avg</code> (Latency Average)</li>
      <li><code>response_prob</code> (Response Probability)</li>
    </ul>
  </li>
  <li>Displays this data using <code>pandas</code> and saves it as a CSV file for further analysis.</li>
</ul>

<h4>7. Exit Option</h4>
<ul>
  <li>The script breaks the main loop and exits when the user selects "Exit".</li>
</ul>

<h3>Enhancements to Consider</h3>
<ul>
  <li><strong>Error Handling:</strong> Although basic error handling is implemented for batch file execution, more robust error handling (e.g., for file reading/writing) would enhance the program’s reliability.</li>
  <li><strong>Logging:</strong> Implementing logging with Python's <code>logging</code> module would help track the program's execution and debug issues.</li>
  <li><strong>Improved User Interaction:</strong> As <code>pyautogui.password()</code> doesn't handle integer validation, consider adding <code>try-except</code> blocks to manage invalid inputs gracefully.</li>
</ul>
