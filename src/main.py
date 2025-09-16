
import os
os.environ["OPENAI_API_REQUESTS_VERIFY"] = "false"
from summarizer import summarize_text


print("Welcome to the AI Productivity Hub - Document Summarizer!")

print("Please choose an option:")
print("1. Summarize a document")
print("2. Exit")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("You chose to summarize a document.")
    file_path = input("Please enter the path to your document (PDF, TXT, DOCX): ")
    print(f"You entered: {file_path}")
    # Try to read the file if it's a .txt file
    if file_path.lower().endswith(".txt"):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            print("File content loaded successfully!")
            print(content)  # Show the content for now
            print("\nSummarizing your document...")
            summary = summarize_text(content)
            print("\nSummary:")
            print(summary)
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("Right now, we only support .txt files. PDF and DOCX support coming soon!")
elif choice == "2":
    print("Goodbye!")
else:
    print("Invalid choice. Please run the program again.")