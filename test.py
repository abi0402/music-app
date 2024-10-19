import syncedlyrics  # Ensure syncedlyrics is correctly installed or available in your Python path
import re
import json

# Function to search for song lyrics and convert to JSON format
def search_and_convert_to_json():
    # Prompt user to enter a song name
    query = input("Enter Song Name: ")
    
    try:
        # Search for lyrics using the syncedlyrics module
        lrc = syncedlyrics.search(query)

        if not lrc:
            print(f"No lyrics found for the song: {query}")
            return

        # Split the data into lines
        lines = lrc.split('\n')

        # Initialize a list to store the JSON entries
        json_data = []

        # Define a regular expression pattern to extract timestamps and text
        pattern = r'\[(\d+:\d+\.\d+)\] (.+)'

        # Loop through each line and extract timestamp and text
        for line in lines:
            match = re.match(pattern, line)
            if match:
                timestamp, text = match.groups()
                json_entry = {
                    "time": timestamp,
                    "lyrics": text
                }
                json_data.append(json_entry)

        # Convert the list of JSON entries to a JSON-formatted string
        json_string = json.dumps(json_data, indent=4)
        
        # Print the JSON string
        print(json_string)
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == '__main__':
    search_and_convert_to_json()
