from pathlib import Path

# Define directory to read from
data_dir = Path("data")

# Check the directory exists
if not data_dir.exists() or not data_dir.is_dir():
    print(f"Directory {data_dir} does not exist or is not a directory.")
else:
    concatenated = ""

    # Loop over each .txt file in the directory
    for child in data_dir.glob("*.txt"):
        if child.is_file():
            try:
                concatenated += child.read_text()
            except Exception as e:
                print(f"Failed to read {child} due to error: {str(e)}")

    if concatenated == "":
        print("No text files found or files are empty.")
    else:
        output_path = "data/out/concatenated.txt"

        try:
            with open(output_path, "w") as f:
                f.write(concatenated)
            print(f"Concatenated file written to {output_path}.")
        except Exception as e:
            print(f"Failed to write concatenated file due to error: {str(e)}")
