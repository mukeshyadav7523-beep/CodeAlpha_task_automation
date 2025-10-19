import re

# Function to extract emails from a text file and save them to another file
def extract_emails(input_file, output_file):
    try:
        # Read the contents of the input file
        with open(input_file, 'r') as f:
            content = f.read()

        # Regular expression for matching email addresses
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

        # Remove duplicate emails
        unique_emails = sorted(set(emails))

        # Write extracted emails to the output file
        with open(output_file, 'w') as f:
            for email in unique_emails:
                f.write(email + '\n')

        print(f"✅ Extraction complete! {len(unique_emails)} email(s) saved to '{output_file}'.")

    except FileNotFoundError:
        print("❌ Error: Input file not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_path = "sample.txt"        # Input text file containing emails
    output_path = "emails_output.txt"  # Output file to save extracted emails

    extract_emails(input_path, output_path)
