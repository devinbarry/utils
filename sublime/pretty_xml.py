import re
import xml.dom.minidom

import sublime
import sublime_plugin


def strip(text):
    return re.sub(r'\s+$', '', text, flags=re.MULTILINE)


def pretty(source, indent):
    doc = xml.dom.minidom.parseString(source)
    return strip(doc.toprettyxml(indent=' '*indent))


class PrettyXmlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get current tab size
        indent = self.view.settings().get('tab_size', 2)

        # Get the current selection
        if self.view.sel()[0].empty():
            region = sublime.Region(0, self.view.size())
            source = self.view.substr(region)
        else:
            region = self.view.sel()[0]
            source = self.view.substr(self.view.sel()[0])

        # Pretty
        result = pretty(source, indent)

        # Replace the buffer
        self.view.replace(edit, region, result)

    def description(self):
        return "Pretty XML"
