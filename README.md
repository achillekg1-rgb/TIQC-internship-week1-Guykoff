### About

**Tools Needed**

* [Gemini Ai](https://gemini.google.com/app)<br/>
* [Cursor](https://cursor.com)<br/><br/>

<ins>**Guide**</ins>

-> [Easy Setup](https://github.com/achillekg1-rgb/TIQC-internship-week1-Guykoff/new/main#easy-setup) <-

-> [Manual Setup](https://github.com/achillekg1-rgb/TIQC-internship-week1-Guykoff/new/main#manual-setup) <-

-> [Help](https://github.com/achillekg1-rgb/TIQC-internship-week1-Guykoff/new/main#help) <-<br/><br/>

## Easy Setup

In order to set this system that calculates the average gpa of individuals combined, You need to make a folder in a directory, preferably in your "*Documents*" folder to make things neat. Name it something that connects to Grades. Next, Download These two Files at the top of this Repository and save them in the newly made folder in the "*Documents*" folder. After that, open your Cursor program you installed, sign in or make an account if you don't have one to access the software then go to the top of your screen and select "*File -> Open File...*" select then open the file named "*students.csv*" to input your own data that you wished to find its total average GPA. Make sure to follow the guide on the first line exactly as it shows (Name,GPA) in order for the system to work. Once you are done inputting your own data, go to "*File -> Save*". After that, You can now run the "*csv-gpa.py*" file and expect a answer from the Terminal at the bottom of your screen. <br/>
> [!IMPORTANT]
> If you change the "*students.csv*" file to another name, Make sure to also change it in the "*csv-gpa.py*" file on Line 6

<br/>

## Manual Setup

In order to set this system that calculates the average gpa of individuals combined, You need to make a folder in a directory, preferably in your "*Documents*" folder to make things neat. Name it something that connects to Grades. Next, In your installed Cursor program, sign in or make an account if you don't have one to have access to the software then go to the top of your screen and select "*File -> New Text File*", then on Line 1, you type "Name,GPA" as your guide (all data put in this file need to exactly follow the same basis of "Name,GPA". GPA has to be a numerical value in order for the system to work) and Line 2 would start with the first person you wish to input in the file and their GPA and switch onto the next line and so on until you finish inserting all the data you need. After you are done doing so, go to "*File -> Save As...*" then open the folder that was made at the start of this instruction (New folder made in "*Documents*") and in the File name field, you can either write your own name or use "*students.csv*". Make sure the file name ends with "*.csv*" or else it won't work (if you can't see it by default type "*.csv*" at the end to make sure it works. After that, you once again create a New Text File by going to "*File -> New Text File*", copy the Source code for the system that calculates the average GPA from below and paste it into the newly made Text File and go to "*File -> Save As...*" and open the Folder that was created to save the file with the student data and save the New Text File as anything you want . This is all that is needed to start pressing the Running the system and give you a response in the Terminal that is located at the bottom of the Cursor software!<br/>
>[!IMPORTANT]
>You save the New Text File as anything you want as long as the File extension ends with "*.py*"<br/>
>If you can't see it by default, type "*.py*" to make sure it works

<br/>

<details>
<summary><ins>Source Code (csv-gpa.py)</ins></summary>

```Python
import csv
import sys
import os

# --- Configuration ---
FILE_NAME = 'students.csv' # If you named the file that has all the data of the students as something else, please change it here. Make sure the file extension still says ".csv"
MAX_GPA = 4.0  # Set the maximum possible GPA for range validation

def calculate_average_gpa(file_path):
    """
    Reads a CSV file, calculates the average GPA, and handles bad rows gracefully.
    A 'bad row' is one that is missing a GPA, has a non-numeric GPA, or has a GPA out of range.
    """
    
    # 1. Setup and Initialization
    total_gpa = 0.0
    student_count = 0
    bad_row_count = 0
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

    # 2. File Handling and Iteration
    try:
        # Use 'with open' for safe file handling
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip the header row (the first row)
            try:
                next(reader) 
            except StopIteration:
                # Handle case where file is empty
                print("The CSV file is empty. No data to process.")
                return

            print(f"--- Processing {FILE_NAME} ---")

            # Loop through the remaining data rows
            for row_index, row in enumerate(reader, start=2): # Start counting from row 2
                
                # 3. Row Validation and Error Handling
                gpa = None
                
                # 3.1 Structure Check: Ensure the row has at least 2 columns ([Name, GPA])
                if len(row) < 2:
                    print(f"[Skipping Row {row_index}]: Missing required GPA column.")
                    bad_row_count += 1
                    continue # Go to the next row

                gpa_str = row[1].strip() # The GPA is expected in the second column (index 1)
                student_name = row[0].strip()

                # 3.2 Type Conversion (The critical try/except block)
                try:
                    gpa = float(gpa_str)
                except ValueError:
                    print(f"[Skipping Row {row_index}]: '{student_name}' has non-numeric GPA: '{gpa_str}'.")
                    bad_row_count += 1
                    continue # Go to the next row

                # 3.3 Range Check
                if not (0.0 <= gpa <= MAX_GPA):
                    print(f"[Skipping Row {row_index}]: '{student_name}' has GPA {gpa:.2f}, which is outside the valid range (0.00 to {MAX_GPA:.2f}).")
                    bad_row_count += 1
                    continue # Go to the next row
                
                # 4. Accumulation (Row is good!)
                total_gpa += gpa
                student_count += 1

    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    # 5. Final Calculation and Output
    
    print("\n--- Results ---")
    
    # Check Count: Handle division by zero if no valid students were found
    if student_count > 0:
        average_gpa = total_gpa / student_count
        
        print(f"Total Valid Students Processed: {student_count}")
        print(f"Total Bad Rows Skipped: {bad_row_count}")
        print("-" * 30)
        # Print the final result formatted to two decimal places
        print(f"Average GPA: {average_gpa:.2f}")
    else:
        print(f"No valid student data found in the file (Skipped {bad_row_count} rows).")
        print("Cannot calculate an average.")

if __name__ == "__main__":  
    calculate_average_gpa(FILE_NAME)
```

</details>

<br/>

## Help

>[!Note]
>If the terminal prints this
>```
>[Skipping Row 2]: 'Charlie Brown' has non-numeric GPA: 'N/A'
>```
>You have not put any numbers but letters after the comma ("Name,GPA"). Please go back to the *students.csv* file and write the number as a numerical value.

<br/>

>[!Note]
>If the terminal prints this
>```
>[Skipping Row 2]: 'Erik Killmonger' has GPA 4.50, which is outside the valid range
>```
>You have to put the correct number between 0.00 and 4.00 range. If you wish to increase the range of the GPA, please go to *line 7* and change the variable to your liking

<br/>

>[!Note]
>If the terminal prints this
>```
>[Skipping Row 2]: Missing required GPA column.
>```
>You did not put any numerical value for the GPA column. In order to fix this, open the *students.csv* file and add the missing values

<br/>

>[!Note]
>If the terminal prints this
>```
>The CSV file is empty. No data to process.
>```
>There is no data in the *students.csv* file. Please open and add the information needed to run the system.

<br/>

>[!Note]
>If the terminal prints this
>```
>Error: The file 'students.csv' was not found.
>```
>The *students.csv* file is in the wrong directory. Please move it into the same folder as the *csv-gpa.py* file.

<br/>

# Documented Tests

<br/>

## Test 1 with intended settings (students.csv contains simulated data)

- Ran the csv-gpa.py script imported from Gemeni
- No execution error from the Terminal 
- Correct file for GPA data record read successfully (multiple files in folder)
- Detected correct row information and printed in Terminal
- Detected incorrect row information and printed in Terminal (Intended)
- Successful use of Function calculating the count of incorrect row information
- Successful use of Function calculating the count of correct row information
- Accurate math data calculation value for Average GPA

**Output**
```Python
PS C:\Users\Achille\Documents\Scripts> & C:/Python314/python.exe c:/Users/Achille/Documents/Scripts/csv-gpa.py
--- Processing students.csv ---
[Skipping Row 4]: 'Charlie Brown' has non-numeric GPA: 'N/A'.
[Skipping Row 6]: 'Erik Killmonger' has GPA 4.50, which is outside the valid range (0.00 to 4.00).
[Skipping Row 7]: Missing required GPA column.

--- Results ---
Total Valid Students Processed: 4
Total Bad Rows Skipped: 3
------------------------------
Average GPA: 3.57
```
<br/>

## Test 2 with intended settigns (students.csv contains simulated data)

- Edited the students.csv to test other fail measures (incorrect file_path)
- Successfully identified incorrect file path for students.csv 
- Terminal successfully printed "Error: The file '{file_path}' was not found"

**Output**
```Python
PS C:\Users\Achille\Documents\Scripts> & C:/Python314/python.exe c:/Users/Achille/Documents/Scripts/csv-gpa.py
Error: The file 'students.csv' was not found.
```
<br/>

## Test 3 with intended settings (students.csv contains simulated data)

- Edited the students.csv to test other fail measures (no data in CSV file)
- Correct file for GPA data record read successfully (returns "The CSV file is empty. No data to process")

**Output**
```Python
PS C:\Users\Achille\Documents\Scripts> & C:/Python314/python.exe c:/Users/Achille/Documents/Scripts/csv-gpa.py
The CSV file is empty. No data to process.
```
<br/>

## Prompts
I asked Gemini to:
> Outline how a script named csv-gpa would read students.csv and print average GPA (two decimals), skipping bad rows.<br/>
> Then i asked to generate the codes i needed to make the system function.
