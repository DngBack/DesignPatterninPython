import json
import re

class JsonProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_json_file()

    def read_json_file(self):
        """Read JSON data from the file."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def remove_html_tags(text):
        """Remove HTML tags from a string."""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def json_to_string(self, data=None, indent_level=0, seen_values=None):
        """Convert JSON data to a formatted string."""
        if data is None:
            data = self.data
        
        if seen_values is None:
            seen_values = set()

        result = []
        indent = ' ' * (indent_level * 4)

        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    result.append(f"{indent}{key}:")
                    result.append(self.json_to_string(value, indent_level + 1, seen_values))
                else:
                    # Remove HTML tags before checking if the value has been seen
                    cleaned_value = self.remove_html_tags(str(value))
                    if cleaned_value not in seen_values:
                        result.append(f"{indent}{key}: {cleaned_value}")
                        seen_values.add(cleaned_value)
        elif isinstance(data, list):
            for item in data:
                result.append(self.json_to_string(item, indent_level + 1, seen_values))
        else:
            # Remove HTML tags before checking if the value has been seen
            cleaned_data = self.remove_html_tags(str(data))
            if cleaned_data not in seen_values:
                result.append(f"{indent}{cleaned_data}")
                seen_values.add(cleaned_data)

        return "\n".join(result)

    def print_formatted_string(self):
        """Print the formatted JSON data."""
        formatted_string = self.json_to_string()
        print(formatted_string)

# Usage
file_path = 'test_1.json'
processor = JsonProcessor(file_path)
processor.print_formatted_string()

