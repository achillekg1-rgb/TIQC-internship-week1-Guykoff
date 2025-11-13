import csv
import sys
import os

# --- Configuration ---
FILE_NAME = 'students.csv'
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
