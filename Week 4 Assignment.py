def read_and_modify_file():
    try:
        # Step 1: Ask the user for the input file name
        input_filename = input("quotes.txt")

        # Step 2: Try to open and read the file
        with open(input_filename, 'r') as infile:
            print("📖 Reading the file...")
            content = infile.readlines()

        # Step 3: Modify the content
        # Example modification: Convert all text to uppercase
        print("🛠️ Modifying the file content (converting to UPPERCASE)...")
        modified_content = [line.upper() for line in content]

        # Step 4: Ask the user for the output file name
        output_filename = input("new_quotes.txt")

        # Step 5: Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"✅ Success! The modified file has been saved as '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist. Please check the filename and try again.")
    except IOError:
        print("❌ Error: There was a problem reading from or writing to the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()