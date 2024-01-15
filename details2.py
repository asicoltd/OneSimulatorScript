import datetime
import subprocess
import os
import pandas as pd
import random
import pyautogui as auto
from pandasgui import show


def options():
    option1 = auto.confirm(text='Select Option', title='Welcome To One Simulator', buttons=['Manual Input', 'Auto Generate', 'Modify Settings', 'Report Summary', 'Exit'])
    if option1 == 'Manual Input':
        option = 1
    elif option1 == 'Auto Generate':
        option = 2
    elif option1 == 'Modify Settings':
        option = 3
    elif option1 == 'Report Summary':
        option = 4
    else:
        option = 5
    return option


# Specify the path to your .bat file
bat_file_path = r'compile.bat'

# Run the .bat file
try:
    subprocess.run(bat_file_path, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the batch file: {e}")

# Specify the path to your .bat file
option = options()

while True:
    if option == 1:
        # Step 1: Open the file for reading
        file_path = 'default_settings.txt'
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Step 2: Prompt the user for the new value for Scenario.endTime
            new_value_end_time = auto.password(
                text='Enter the new value for Scenario.endTime (e.g., 128891):', title='', default='', mask='')

            # If the user cancels, go back to the main menu
            if new_value_end_time is None:
                option = options()
                continue

            new_value_end_time = int(new_value_end_time)

            # Step 3: Get the current date and time
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")

            formatted_router = auto.confirm(
                text='Select A Router', title='Router', buttons=['EpidemicRouter', 'SprayAndWaitRouter', 'ProphetRouter'])

            # Step 4: Iterate through the lines and update the line containing "Scenario.endTime =" and "Scenario.name = default_scenario"
            modified_lines = []
            for line in lines:
                if line.strip().startswith("Scenario.endTime ="):
                    modified_lines.append(f"Scenario.endTime = {new_value_end_time}\n")
                elif line.strip().startswith("Scenario.name ="):
                    modified_lines.append(f"Scenario.name = {formatted_router}_{formatted_datetime}\n")
                elif line.strip().startswith("Group.router ="):
                    modified_lines.append(f"Group.router = {formatted_router}\n")
                else:
                    modified_lines.append(line)

            # Step 5: Open the same file for writing and write the modified content
            with open(file_path, 'w') as file:
                file.writelines(modified_lines)

        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            exit()

        bat_file_path = r'one.bat -b 1'

        # Run the .bat file
        try:
            subprocess.run(bat_file_path, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running the batch file: {e}")

        option = options()
    elif option == 2:
        Router = auto.confirm(text='Select A Option', title='Router',
                              buttons=['Randomly generate all routing', 'EpidemicRouter', 'SprayAndWaitRouter',
                                       'ProphetRouter', 'Cancel'])

        if Router == 'Cancel':
            option = options()
            continue

        LoopNo = auto.password(text='How many loops do you want to run (e.g., 5):', title='Loop no (0 for Exit)', default='', mask='')

        # If the user cancels, go back to the main menu
        if LoopNo is None:
            option = options()
            continue

        LoopNo = int(LoopNo)

        if LoopNo != 0:
            for i in range(LoopNo):
                # Step 1: Open the file for reading
                file_path = 'default_settings.txt'
                try:
                    with open(file_path, 'r') as file:
                        lines = file.readlines()

                    # Step 2: Prompt the user for the new value for Scenario.endTime
                    new_value_end_time = random.randrange(4200, 172800)
                    if Router == 'ProphetRouter':
                        new_value_end_time = random.randrange(4200, 50000)
                    print(f"Generated Scenario.endTime: {new_value_end_time}")
                    # Step 3: Get the current date and time
                    current_datetime = datetime.datetime.now()
                    formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")

                    formatted_router = ''
                    if (Router == 'Randomly generate all routing'):
                        r = random.randrange(1, 4)
                    else:
                        if Router == 'EpidemicRouter':
                            r = 1
                        elif Router == 'SprayAndWaitRouter':
                            r = 2
                        else:
                            r = 3
                    if r == 1:
                        formatted_router = 'EpidemicRouter'
                    elif r == 2:
                        formatted_router = 'SprayAndWaitRouter'
                    elif r == 3:
                        formatted_router = 'ProphetRouter'

                    print(f"Iteration {i}, selected router: {formatted_router}")

                    # Step 4: Iterate through the lines and update the line containing "Scenario.endTime =" and "Scenario.name = default_scenario"
                    modified_lines = []
                    for line in lines:
                        if line.strip().startswith("Scenario.endTime ="):
                            modified_lines.append(f"Scenario.endTime = {new_value_end_time}\n")
                        elif line.strip().startswith("Scenario.name"):
                            modified_lines.append(f"Scenario.name = {formatted_router}_{formatted_datetime}\n")
                        elif line.strip().startswith("Group.router ="):
                            modified_lines.append(f"Group.router = {formatted_router}\n")
                        else:
                            modified_lines.append(line)

                    # Step 5: Open the same file for writing and write the modified content
                    with open(file_path, 'w') as file:
                        file.writelines(modified_lines)
                except FileNotFoundError:
                    print(f"File '{file_path}' not found.")
                    exit()

                bat_file_path = r'one.bat -b 1'

                # Run the .bat file
                try:
                    subprocess.run(bat_file_path, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error running the batch file: {e}")

        option = options()
    elif option == 3:
        # Modify Simulation Settings
        settings_to_modify = auto.confirm(text='Select setting to modify:',
                                          title='Modify Settings',
                                          buttons=['Transmit Speed', 'Transmit Range', 'Number of Hosts', 'Cancel'])

        if settings_to_modify == 'Cancel':
            option = options()
            continue

        file_path = 'default_settings.txt'
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            if settings_to_modify == 'Transmit Speed':
                example_range = '[100k, 1M]'
            elif settings_to_modify == 'Transmit Range':
                example_range = '[5, 20]'
            elif settings_to_modify == 'Number of Hosts':
                example_range = '[20, 50]'

            # Prompt the user for the new value
            new_value = auto.password(
                text=f'Enter the new value for {settings_to_modify} {example_range}:',
                title='',
                default='',
                mask='')

            # If the user cancels, go back to the main menu
            if new_value is None:
                option = options()
                continue

            # Iterate through the lines and update the selected setting
            modified_lines = []
            for line in lines:
                if settings_to_modify == 'Transmit Speed' and line.strip().startswith("highspeedInterface.transmitSpeed"):
                    modified_lines.append(f"highspeedInterface.transmitSpeed = {new_value}\n")
                elif settings_to_modify == 'Transmit Range' and line.strip().startswith("highspeedInterface.transmit"):
                    modified_lines.append(f"highspeedInterface.transmitRange = {new_value}\n")
                elif settings_to_modify == 'Number of Hosts' and line.strip().startswith("Group.nrofHosts"):
                    modified_lines.append(f"Group.nrofHosts = {new_value}\n")
                else:
                    modified_lines.append(line)

            # Open the same file for writing and write the modified content
            with open(file_path, 'w') as file:
                file.writelines(modified_lines)

        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            exit()

        bat_file_path = r'one.bat -b 1'

        # Run the .bat file
        try:
            subprocess.run(bat_file_path, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running the batch file: {e}")

        option = options()
    elif option == 4:
        folder_path = os.getcwd()
        print(folder_path)
        folder_path = '../one_1.4.1/reports'
        # Retrieve all files in the folder
        files = os.listdir(folder_path)

        # Filter files that start with "abc" and have a .txt extension #### file.startswith('') and
        text_files = [file for file in files if file.endswith('.txt')]

        # Iterate over each text file and extract the text
        text_data = []
        for file in text_files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'r') as f:
                text = f.read()
                text_data.append(text)
        # Delivery Probability, Overhead Ratio, Latency, Response Probability
        fileName = []
        delProbs = []
        overHeadRats = []
        latencys = []
        RespProbs = []

        # Print the extracted text from each file
        for text in text_data:
            # Split the data into lines
            lines = text.split('\n')

            # Extract the column names and values
            column_names = []
            values = []
            print(lines[0])
            column_names.append("FileName")
            filename = lines[0].split('Message stats for scenario')
            values.append(filename[1])
            for line in lines:
                if ':' in line:
                    key, value = line.split(': ')
                    column_names.append(key)
                    try:
                        value = float(value)
                    except ValueError:
                        if value == 'NaN':
                            value = 0
                    values.append(value)

            for i in range(len(column_names)):
                if column_names[i] == 'FileName':
                    fileName.append(values[i])
                if column_names[i] == 'delivery_prob':
                    delProbs.append(values[i])
                if column_names[i] == 'overhead_ratio':
                    overHeadRats.append(values[i])
                if column_names[i] == 'latency_avg':
                    latencys.append(values[i])
                if column_names[i] == 'response_prob':
                    RespProbs.append(values[i])
        df = pd.DataFrame(fileName, columns=['FileName'])
        df['delivery_prob'] = delProbs
        df['overhead_ratio'] = overHeadRats
        df['latency_avg'] = latencys
        df['response_prob'] = RespProbs

        avg = sum(delProbs) / len(delProbs)
        print("Average of delivery Probability", avg)
        avg = sum(overHeadRats) / len(overHeadRats)
        print("Average of overhead Ratio", avg)
        avg = sum(latencys) / len(latencys)
        print("Average of latency Average", avg)
        avg = sum(RespProbs) / len(RespProbs)
        print("Average of response Probability", avg)
        print(df)
        show(df)
        df.to_csv('out.csv')
        auto.alert(text=len(df)+" data(s)", title='Total data', button='OK')
        option = options()
    elif option == 5:
        break
