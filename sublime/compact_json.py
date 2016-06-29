import json
import re

import sublime
import sublime_plugin


def strip(text):
    return re.sub(r'\s+$', '', text, flags=re.MULTILINE)


def compact(source):
    return strip(json.dumps(json.loads(source), sort_keys=True))


class CompactJsonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get the current selection
        if self.view.sel()[0].empty():
            region = sublime.Region(0, self.view.size())
            source = self.view.substr(region)
        else:
            region = self.view.sel()[0]
            source = self.view.substr(self.view.sel()[0])

        # Unpretty
        result = compact(source)

        # Replace the buffer
        self.view.replace(edit, region, result)

    def description(self):
        return "Compact Json"
