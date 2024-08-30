# Best Ever Plugin (Example Sublime Text Plugin)

This enumerates some of the content that may be needed to build a plugin suitable for
submission to Package Control. It's primarily focused on pure python functional plugins;
those with binaries, syntax, and color schemes are a bit different - maybe doc later.
Adjust to taste.

For this example, names are:
- `Best Ever Plugin` is the human-friendly name, and appears in menus and the Command Palette.
- `example_plugin` is the repo name.
Give serious thought to name selections as refactoring them becomes a real pain.

Note that this addresses GitHub only. BitBucket should be a straightforward translation.


## Installation
From the Command Palette, run `Package Control: Install Package` command.
In the packages list, find the package name you are interested in and install it.

## Usage

Add detail to the Overview such as how-to, images, videos, references, caveats, ...

## Commands and Menus

Describe the commands supplied by this package and how they are presented in menus.

| Command              | Description      | Args             |
| :--------            | :-------         | :--------        |
| example_run          | words...         | words...         |
| example_terminal     | words...         | words...         |
| example_tree         | words...         | words...         |


It's considered good practice to not add a Package specific `Context.sublime-menu` file
as it clogs up the menu real estate. Either provide a file with command examples or simply describe them here.
Suggest the entries the user can add to their own `Context.sublime-menu` files. Typical entries are:
``` json
{ "caption": "Run", "command": "example_run" },
{ "caption": "Terminal Here", "command": "example_terminal" },
{ "caption": "Tree", "command": "example_tree" },
```

While not quite as critical, it's still generally a good idea to do the same for the other
`*.sublime-menu` files. One exception to that is `Main.sublime-menu` which should be used
minimally to provide `Preferences` for the Package - [like this](Main.sublime-menu).

Finally, you can optionally include `Default.sublime-commands` to populate the Command Palette.
Some packages prefer to use only Main and Context menus instead. Note that `Default` is
only convention; any name will work.


## Settings

Provide a description of all settings in your `example_plugin.sublime-settings` file.

| Setting           | Description      | Options        |
| :--------         | :-------         | :------        |
| example_color     | words...         | words...       |
| example_size      | words...         | words...       |


# Publishing To Package Control

Most of this is covered well in https://packagecontrol.io/docs/submitting_a_package but a few notes are worth mentioning.

It is assumed you have forked https://github.com/wbond/package_control_channel.

## Package Repository

To add a package, you add an entry to one of the `package_control_channel\repository\*.json` files.
The specific file is the one with the first letter of the `name`. In our case it would go in `b.json`

A basic and usually adequate repository entry is (for this example):
```json
{
    "name": "Best Ever Plugin",
    "details": "https://github.com/<user>/example_plugin",
    "labels": [ "best", "ever" ],
    "releases": [
        {
            "sublime_text": ">4000",
            "platforms":["windows", "linux"],
            "tags": true
        }
    ]
},
```

It must be placed in exact alphabetical order by `name`, and use tabs not spaces.
`ChannelRepositoryTools: Test Default Channel` command will remind you of that of course.

Labels should be taken from a short list of standard names. At this writing there are 1700+
different names in use, with many being something no one will ever search on. And keep them short:
use `debug` not `debugger` and be found.

For power users, more options are described here:
https://github.com/wbond/package_control/blob/master/example-repository.json.


## Questionnaire

When you execute your PR, you are presented with a questionnaire. It's probably easier to populate
that in advance. The content is roughly this:
```
<!--
The manual review may take several days or weeks, depending on the reviewer's availability and workload.
Patience padawan!

You can request a review from @packagecontrol-bot. Please ensure the reviews pass and follow any instructions.

Please provide some information via this checklist, feel free to remove what't not applicable.
-->

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


<!--
*)   Unless it definitely really needs them, they apply to the cursor's context
     and their visibility is conditional. Space in this menu is limited!
**)  There aren't enough keys for all packages, you'd risk overriding those of other packages.
     You can put commented out suggestions in a keymap file, and/or explain how to create bindings in your README.
***) We have hundreds of color schemes, and plenty of scopes to make any syntax work.

For bonus points also considered how the review guidelines apply to your package:
https://github.com/wbond/package_control_channel/wiki#reviewing-a-package-addition

For updates to existing packages: If your package isn't using tag based releases, please switch to tags now.
-->

[1]: https://packagecontrol.io/docs/submitting_a_package
[2]: https://semver.org
[3]: https://www.git-scm.com/docs/gitattributes#_export_ignore
```

## Updating a Package

To update a previously published package simply update the plugin code, push and
tag with the new version number. No need to touch the `package_control_channel` contents.
Package Control will update the local user's copy on a periodic basis.

Depending on the scope of the change, it may be polite to inform the user using the
https://packagecontrol.io/docs/messaging capability.


## Multiple Package Development

If you are developing more than one package at the same time, there are a couple of other
things that need to happen. Instead of working directly on the fork and issuing a PR
from there, you need to branch your fork for each plugin. To submit a branch, switch to it,
run `ChannelRepositoryTools: Test Default Channel`, push, and PR.

Ref: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork


## Package Metadata

Package Control generates `package-metadata.json` which is added to the final package.
Most fields come from your repository.json entry except as noted.
Note that not all fields are required and some may not be present depending on the
repository schema the plugin was created with.

```json
{
    "description": "An example demonstrating a Sublime Text plugin.", // From the github repo About.
    "platforms":["windows", "linux"],
    "version": "1.2.3",  // Most recent semantic version tag in the repo.
    "sublime_text": ">4000",
    "python_version": "3.3", // From .python-version if available?
    "url": "https://github.com/cepthomas/example_plugin",
    "issues": "https://github.com/cepthomas/example_plugin/issues",
    "author": ["cepthomas"],
    "labels": ["best", "ever"],
    // It appears dependencies was in earlier schemas and was replaced by libraries in later schemas.
    // See https://packagecontrol.io/docs/dependencies.
    "dependencies": ["???"],
    "libraries": ["???"],
    "install_time": 123.456, // From Package Control.
    "release_time": "2099-01-01 00:00:00", // From Package Control.
    "upgrade_time": 777.888 // From Package Control.
}
```


# All The Files

## User Data

Nearly all of the interesting files for users live here.

```
$APPDATA\Sublime Text
|
+---Installed Packages --> Installed by Sublime or via Package Control.
|       *.sublime-package
|
+---Lib --> As required by Installed or User Packages.
|   +---python33
|   \---python38
|
+---Local
|       Session.sublime_session --> Contains project history - edit with different editor to clean up.
|       *.sublime_session --> Backups and caches.
|
\---Packages --> Loose packages, not from Package Control. Where you create your plugin.
    |
    +---Default --> To override the builtin menus, first copy them here from Default.sublime-package
                    and comment out your exclusions.
    |       Context.sublime-menu
    |       Side Bar.sublime-menu
    |
    +---example_plugin --> This example plugin.
    |   |   .gitattributes
    |   |   .gitignore
    |   |   .python-version
    |   |   Default.sublime-commands
    |   |   LICENSE
    |   |   Main.sublime-menu
    |   |   example_plugin.sublime-settings
    |   |   README.md
    |   |   source1.py
    |   |   source2.py
    |   |   README.md --> This file.
    |   |   --> Could also have stuff like:
    |   |   *.tmLanguage
    |   |   *.sublime-syntax
    |   |   *.sublime-color-scheme
    |   |   *.sublime-keymap
    |   |
    |   \---test
    |           some_test_code.py
    |
    \---User -->
            *.sublime-settings --> User settings for installed packages.
            Context.sublime-menu --> Add stuff to the default menu.
            Main.sublime-menu --> Ditto.
            Side Bar.sublime-menu --> Ditto.
            Tab Context.sublime-menu --> Ditto.
            My.sublime-color-scheme --> Personal/custom.
            Default (Windows/Linux/OSX).sublime-keymap --> Personal/custom.
```


## ST Executable Dir

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
