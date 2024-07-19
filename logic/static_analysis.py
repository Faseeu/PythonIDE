import subprocess

class StaticAnalysis:
    @staticmethod
    def run_analysis(file_path):
        try:
            result = subprocess.run(['mypy', file_path], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"An error occurred: {str(e)}"
