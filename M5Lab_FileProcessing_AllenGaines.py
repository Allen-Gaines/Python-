# Program to read patient data, calculate BMI, and write results to files
# 2025-06-26
# CSC121 M5Lab
# Allen Gaines

# Step 1: Create a sample patients.txt file
with open("patients.txt", "w") as file:
    file.write("patient-id,height,weight\n")
    file.write("P0123,66,150\n")
    file.write("P4354,68,164\n")
    file.write("P9999,abc,200\n")  # Invalid height
    file.write("P7777,70,xyz\n")   # Invalid weight

# Function to check if a value is numeric (for floats)
def is_number(value):
    return value.replace(".", "", 1).isdigit()

# Function to calculate BMI
def calculate_bmi(height, weight):
    return (weight / (height ** 2)) * 703

# Main program: read file, process data, and write output files
def process_patient_data():
    bmi_lines = []
    csv_lines = ["patient-id,height,weight,BMI"]

    with open("patients.txt", "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue  # Skip bad line format

            patient_id, height_str, weight_str = parts

            if is_number(height_str) and is_number(weight_str):
                height = float(height_str)
                weight = float(weight_str)
                bmi = calculate_bmi(height, weight)
                print(f"Patient ID: {patient_id}, BMI: {bmi:.2f}")
                bmi_lines.append(f"{patient_id},{bmi:.2f}")
                csv_lines.append(f"{patient_id},{height},{weight},{bmi:.2f}")
            else:
                print(f"Error: Non-numeric height or weight for patient ID {patient_id}")

    # Part 2: Write BMI to bmi.txt
    with open("bmi.txt", "w") as bmi_file:
        for line in bmi_lines:
            bmi_file.write(line + "\n")

    # Part 4: Write full data to patient_bmi.csv
    with open("patient_bmi.csv", "w") as csv_file:
        for line in csv_lines:
            csv_file.write(line + "\n")

# Run the program
process_patient_data()
