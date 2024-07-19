import subprocess

class Formatter:
    @staticmethod
    def format_code(file_path):
        try:
            result = subprocess.run(['black', file_path], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"An error occurred: {str(e)}"
