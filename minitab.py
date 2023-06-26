import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()

def replace_column_values(data, selected_columns, column_to_replace, replacement_value):
    # Extract the desired columns
    extracted_data = data[selected_columns].copy()

    # Replace a column with a specific value
    extracted_data[column_to_replace] = replacement_value

    return extracted_data

# Prompt the user for multiple filenames
while True:
    filenames = input("Enter the filenames (comma-separated): ").split(",")
    all_files_exist = True

    # Check if all files exist
    for filename in filenames:
        if not os.path.isfile(filename):
            print(f"File not found: {filename}")
            all_files_exist = False
            break

    if all_files_exist:
        break
    else:
        print("Please try again.")

# Prompt the user for column names
selected_columns = ['SampleID','Polybead/BackPressure']
column_to_replace = 'SampleID'

# Create an empty list to store the appended data frames
appended_data = []

# Iterate over each filename
for filename in filenames:
    # Prompt the user for the replacement value
    replacement_value = input(f"Enter the replacement value for {filename}: ")

    # Read the CSV file into a DataFrame
    data = pd.read_csv(filename)

    # Call the function to replace column values
    modified_data = replace_column_values(data, selected_columns, column_to_replace, replacement_value)

    # Append the modified data to the appended_data list
    appended_data.append(modified_data)

# Concatenate the data frames in the list
merged_data = pd.concat(appended_data)

# Reset the index of the merged data
merged_data.reset_index(drop=True, inplace=True)

# Prompt the user for the output filename
output_filename = input("Enter the output filename: ")

# Write the merged data to a CSV file
merged_data.to_csv(output_filename, index=False)

print(f"The merged data has been written to {output_filename}.")




'''
# Prompt the user for column names and replacement value
selected_columns = ['AssayName','SampleID']
column_to_replace = 'SampleID'
replacement_value = 'type'

'''