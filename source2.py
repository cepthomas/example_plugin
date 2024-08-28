import os
import re
import json
import sublime
import sublime_plugin


# All the command handlers.


#-----------------------------------------------------------------------------------
class ExampleRunCommand(sublime_plugin.TextCommand):
    '''Doc'''

    def run(self, edit):
        sublime.message_dialog('Run!!')


#-----------------------------------------------------------------------------------
class ExampleTerminalCommand(sublime_plugin.TextCommand):
    '''Doc'''

    def run(self, edit):
        sublime.message_dialog('Terminal!!')


#-----------------------------------------------------------------------------------
class ExampleTreeCommand(sublime_plugin.TextCommand):
    '''Doc'''

    def run(self, edit):
        sublime.message_dialog('Tree!!')
