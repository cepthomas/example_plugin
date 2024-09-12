import os
import re
import json
import sublime
import sublime_plugin


# All the command handlers.


#-----------------------------------------------------------------------------------
class ExampleFooCommand(sublime_plugin.TextCommand):
    '''Doc'''

    def run(self, edit):
        sublime.message_dialog('Foo!!')


#-----------------------------------------------------------------------------------
class ExampleBarCommand(sublime_plugin.TextCommand):
    '''Doc'''

    def run(self, edit):
        sublime.message_dialog('Bar!!')

