# Best Ever Plugin (Example Sublime Text Plugin)

This identifies most of the content that is needed to build a plugin suitable for
submission to Package Control. It describes a basic pure python functional plugin.
Those with binaries, syntax, or color schemes are a bit different - TBD.
Adjust to taste.

For this example, primary names are:
- `Best Ever Plugin`: the user facing friendly-name, name of the local clone, and appears in menus, settings, command palette, etc.
- `ExamplePlugin`: name for internals.
- `https://github.com/<user>/example_plugin.git`: the repo-name, can be anything.

Give serious thought to name selections as refactoring them can become a real pain.

Assumes ST4 but should be easily retrofitted for ST3. ST2 is right out.

Note that this assumes GitHub though BitBucket should be a straightforward translation.


## Installation

You may want to add installation steps here, maybe something like this:

*From the Command Palette, run `Package Control: Install Package` command.
In the packages list, find the package friendly-name you are interested in and install it.*

## Usage

Add any pertinent details such as how-to, images, videos, references, caveats, ...

## Commands and Menus

Describe the commands supplied by this package and how they are presented in menus.

| Command              | Description      | Args             |
| :--------            | :-------         | :--------        |
| example_foo          | words...         | words...         |
| example_bar          | words...         | words...         |


It's considered good practice to not add a Package specific `Context.sublime-menu` file
as it clogs up the context menu real estate. Either provide a file with command examples or simply describe them here.
Suggest the entries the user can add to their own `Packages\User\Context.sublime-menu` file:
``` json
{ "caption": "Foo", "command": "example_foo" },
{ "caption": "Bar", "command": "example_bar" },
```

While not quite as critical, it's still generally a good idea to do the same for the other
`*.sublime-menu` files. One exception to that is `Main.sublime-menu` which should be used
minimally to provide `Preferences` for the Package - [like this](Main.sublime-menu).

Finally, you can optionally include `Default.sublime-commands` to populate the Command Palette.
Some packages prefer to use only Main and Context menus instead. Note that `Default` is
only convention; any name will work.


## Settings

Provide a description of all settings in your `Best Ever Plugin.sublime-settings` file.

| Setting           | Description      | Options        |
| :--------         | :-------         | :------        |
| example_color     | words...         | words...       |
| example_size      | words...         | words...       |


# Publishing To Package Control

Most of this is covered well in https://packagecontrol.io/docs/submitting_a_package but a few notes are worth mentioning.

It is assumed you have forked https://github.com/wbond/package_control_channel.

## Package Repository

To add a package, you add an entry to one of the `package_control_channel/repository/*.json` files.
The specific file is the one with the first letter of the friendly-name. In our case it would go in `b.json`

A basic and usually adequate repository entry is (for this example):
```json
{
    "name": "Best Ever Plugin",                             // friendly-name
    "details": "https://github.com/<user>/example_plugin",  // repository
    "labels": [ "best", "ever" ],                           // see below
    "releases": [
        {
            "sublime_text": ">=3000",          // min sublime version required
            "platforms":["windows", "linux"],  // applicability
            "tags": true                       // always true (for this schema)
        }
    ]
},
```

It must be placed in exact alphabetical order by friendly-name, and use tabs not spaces.
`ChannelRepositoryTools: Test Default Channel` command will remind you of that of course.

Labels should be taken from a short list of standard labels. At this writing there are 1700+
different labels in use, with many being something no one will ever search on. And keep them short:
use `debug` not `debugger` and it is more likely to be found. Start with the list found in:
https://github.com/wbond/package_control/blob/master/example-repository.json.


For power users, there are many more repository options described in the example file.


## Questionnaire

When you execute your PR, you are presented with a questionnaire. It's easier to prep
and populate in advance. The content is roughly this:
```
- [ ] I'm the package's author and/or maintainer.
- [ ] I have read [the docs][1].
- [ ] I have tagged a release with a [semver][2] version number.
- [ ] My package repo has a description and a README describing what it's for and how to use it.
- [ ] My package doesn't add context menu entries. *
- [ ] My package doesn't add key bindings. **
- [ ] Any commands are available via the command palette.
- [ ] Preferences and keybindings (if any) are listed in the menu and the command palette, and open in split view.
- [ ] If my package is a syntax it doesn't also add a color scheme. ***
- [ ] If my package is a syntax it is named after the language it supports (without suffixes like "syntax" or "highlighting").
- [ ] I use [.gitattributes][3] to exclude files from the package: images, test files, sublime-project/workspace.

My package is ...

There are no packages like it in Package Control.
<!-- OR -->
My package is similar to ... However it should still be added because ...
```

## Updating a Package

To update a previously published package simply update the plugin code, push and
tag with the new version number. There is no need to touch the `package_control_channel` contents.
Package Control will update the local user's copy on a periodic basis.

Depending on the scope of the change, it may be polite to describe the changes to the user using the
https://packagecontrol.io/docs/messaging capability.


## Multiple Package Development

If you are developing more than one package at the same time, there are a couple of other
things that need to happen. Instead of working directly on the fork and issuing a PR
from there, you need to branch your fork for each plugin. To submit a branch, switch to it,
run `ChannelRepositoryTools: Test Default Channel`, commit, push, and PR per the Package Control
instructions.

Ref: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork


# Reference

Extra reading material.

## Package Metadata

Package Control generates `package-metadata.json` which is added to the final package.
This should never be created or modified by the plugin author.
Most fields come from your edited `package_control_channel\repository\*.json` entry except as noted.
Note that not all fields are required and some may not be present depending on the
repository schema the plugin was created with.

```json
{
    "description": "An example demonstrating a Sublime Text plugin.", // From the github repo About.
    "platforms":["windows", "linux"],
    "version": "1.2.3",  // Most recent semantic version tag in the repo.
    "sublime_text": ">4000",
    "python_version": "3.3", // From .python-version (if available)?
    "url": "https://github.com/<user>/example_plugin",
    "issues": "https://github.com/<user>/example_plugin/issues",
    "author": ["<user>"],
    "labels": ["best", "ever"],
    // ? It appears dependencies was in earlier schemas and was replaced by libraries in later schemas.
    // See https://packagecontrol.io/docs/dependencies.
    "dependencies": ["???"],
    "libraries": ["???"],
    "install_time": 123.456, // From Package Control.
    "release_time": "2099-01-01 00:00:00", // From Package Control.
    "upgrade_time": 777.888 // From Package Control.
}
```


## User Data Files

Nearly all of the interesting files for users live here.

```
<APPDATA>\Sublime Text
|
+---Installed Packages --> Installed by Sublime or via Package Control.
|       *.sublime-package
|
+---Lib --> As required by Installed or User Packages.
|   +---python33
|   \---python38
|
+---Local
|       Session.sublime_session --> Contains project history - edit with a different editor to clean up.
|       *.sublime_session --> Backups and caches.
|
\---Packages --> Loose packages, not from Package Control. This is where you create your plugin.
    |
    |   ExamplePlugin.sublime-settings -> user settings for plugin
    |
    +---Default --> To override the built-in menus, copy them here from `Default.sublime-package`
    |               and comment out exclusions. Warning - this is brittle when updating ST versions.
    |       Main.sublime-menu
    |       Context.sublime-menu
    |       Side Bar.sublime-menu
    |
    +---ExamplePlugin --> This example plugin.
    |   |   .gitattributes
    |   |   .gitignore
    |   |   .python-version
    |   |   Default.sublime-commands
    |   |   Main.sublime-menu
    |   |   ExamplePlugin.sublime-settings -> default settings for plugin
    |   |   example.py
    |   |   commands.py
    |   |   README.md
    |   |   LICENSE
    |   |   ... Could also have stuff like:
    |   |   *.tmLanguage
    |   |   *.sublime-syntax
    |   |   *.sublime-color-scheme
    |   |   *.sublime-keymap
    |   |
    |   \---tests
    |           some_test_code.py
    |
    +---User --> Customizations
    |       *.sublime-settings --> User settings for installed packages.
    |       Context.sublime-menu --> Add stuff to the default menu.
    |       Main.sublime-menu --> etc.
    |       Side Bar.sublime-menu --> etc.
    |       Tab Context.sublime-menu --> etc.
    |       My.sublime-color-scheme --> Personal/custom.
    |       Default (Windows/Linux/OSX).sublime-keymap --> Personal/custom.
    |
    \---ExamplePlugin --> plugin storage area
            my.log
            other_+-config.json
```


## Executable Files

Not really pertinent but for the sake of completeness.

```
$EXEDIR\Sublime Text
|
|   subl.exe
|   sublime_text.exe
|   sublime.py
|   sublime_plugin.py
|   plugin_host-3.3.exe
|   plugin_host-3.8.exe
|   python33.dll
|   python38.dll
|   ...
+---Lib
|   +---python3
|   \---python33
|           sublime.py
|           sublime_plugin.py
|           sublime_types.py
|   \---python38
|           sublime.py
|           sublime_plugin.py
|           sublime_types.py
\---Packages --> factory defaults
        Default.sublime-package  --> Default ST internals and packages.
        *.sublime-package
```
