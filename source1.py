import os
import re
import json
import sublime
import sublime_plugin


# Infrastructure.


# Definitions.
SETTINGS_FILE = "example_plugin.sublime-settings"


#-----------------------------------------------------------------------------------
def plugin_loaded():
    '''Called per plugin instance.'''
    print(f'plugin_loaded() {__package__}')


#-----------------------------------------------------------------------------------
def plugin_unloaded():
    '''Ditto.'''
    pass


#-----------------------------------------------------------------------------------
class ExamplePluginEvent(sublime_plugin.EventListener):
    '''Listen for events of interest.'''

    def on_init(self, views):
        '''First thing that happens when plugin/window created.'''
        settings = sublime.load_settings(SETTINGS_FILE)

    def on_load_project(self, window):
        '''This gets called for new windows.'''

    def on_pre_close_project(self, window):
        '''Save to file when closing window/project.'''

    def on_load(self, view):
        '''Load a file.'''

    def on_post_save(self, view):
        '''Refresh.'''
