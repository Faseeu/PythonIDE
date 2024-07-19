import subprocess

class Linter:
    @staticmethod
    def run_linter(file_path):
        try:
            result = subprocess.run(['ruff', file_path], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"An error occurred: {str(e)}"
