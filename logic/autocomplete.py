import jedi

class AutoComplete:
    @staticmethod
    def get_completions(source_code, line, column):
        script = jedi.Script(source_code, line, column)
        completions = script.complete()
        return [completion.name for completion in completions]
