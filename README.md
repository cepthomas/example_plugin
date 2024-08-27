# The Best Plugin for Sublime Text

This enumerates some of the content that may be needed to build a plugin suitable for
submission to Package Control. It's primarily focused on pure python functional plugins;
those with binaries, syntax, and color schemes are a bit different - maybe later. Adjust to taste.

## Overview
Use this first section to describe what it does at a fairly high level.
`The Best Plugin` is the human-friendly name, appears in menus, pkg control.
`example_plugin` is the repo name.

## Installation
From the `Command Palette`, run `Package Control: Install Package` command.
In the opened packages list, find the package name and install it.

## Usage

Add detail to the Overview such as how-to, images, videos, references, caveats, ...

## Commands
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

While not quite as critical, it's still generally a good idea to do the same for the other `*.sublime-menu`
files. One exception to that is `Main.sublime-menu` which should be used minimally to provide `Preferences`
for the Package - [See this](Main.sublime-menu).

Finally, you can optionally include `Default.sublime-commands` to populate the `Command Palette` selector.
Some packages prefer Main and Context menus instead. Note that `Default` is convention; any name will work.


## Settings

Provide a description of all settings in your `example_plugin.sublime-settings` file.

| Setting           | Description      | Options        |
| :--------         | :-------         | :------        |
| example_color     | words...         | words...       |
| example_size      | words...         | words...       |


# Publishing to Package Control

Most of this is covered well in [Submitting A Package](https://packagecontrol.io/docs/submitting_a_package)
but a few notes are worth mentioning.


## Package repo entry:

C:\Dev\repos\Misc\package_control_channel\repository\

In C:\Dev\repos\Misc\package_control_channel\repository\m.json

```json
{
    "name": "The Best Plugin",
    "details": "https://github.com/<user>/example_plugin",
    "labels": [ "howto", "utilities" ],
    "releases": [
        {
            "sublime_text": ">4000",
            "tags": true
        }
    ]
},
```

## Questionnaire
When you execute your PR, you are presented with a questionnaire. It's probably easier to do that in advance.
The content is roughly this:
```
<!--
The manual review may take several days or weeks,
depending on the reviewer's availability and workload.
Patience padawan!

You can request a review from @packagecontrol-bot.
Please ensure the reviews pass and follow any instructions.

Please provide some information via this checklist,
feel free to remove what't not applicable.
-->

- [ ] I'm the package's author and/or maintainer.
- [ ] I have have read [the docs][1].
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
*)   Unless it definitely really needs them,
     they apply to the cursor's context
     and their visibility is conditional.
     Space in this menu is limited!
**)  There aren't enough keys for all packages,
     you'd risk overriding those of other packages.
     You can put commented out suggestions in a keymap file, 
     and/or explain how to create bindings in your README.
***) We have hundreds of color schemes,
     and plenty of scopes to make any syntax work. 

For bonus points also considered how the review guidelines apply to your package:
https://github.com/wbond/package_control_channel/wiki#reviewing-a-package-addition

For updates to existing packages:
If your package isn't using tag based releases,
please switch to tags now.
 -->

[1]: https://packagecontrol.io/docs/submitting_a_package
[2]: https://semver.org
[3]: https://www.git-scm.com/docs/gitattributes#_export_ignore
```


## Simultaneous ==========

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork



## ??

Package Control generates `package-metadata.json`. Most fields come from Package repo entry.

```json
{
    "description": "Efficiently format, edit, arrange, and evaluate cells in CSV files", // from github "About"
    "dependencies": [],
    "platforms": ["*"],
    "url": "https://github.com/wadetb/Sublime-Text-Advanced-CSV",
    "version": "1.1.9",
    "sublime_text": "*"
}
```



# All the Files

## ST Executable Dir

 X is 3 and/or 8.

```
|   subl.exe
|   sublime_text.exe
|   sublime.py
|   sublime_plugin.py
|   plugin_host-3.X.exe
|   python3X.dll
|   ...
+---Lib
|   |   python3.X.zip
|   +---python3
|   \---python3X
|           sublime.py
|           sublime_plugin.py
|           sublime_types.py
\---Packages --> factory defaults
        Default.sublime-package  --> default ST internals and packages
        *.sublime-package
```

## User Data

Nearly all of the interesting files for users live in $APPDATA\Sublime Text.

```
+---Installed Packages --> User packages, including those installed via Package Control.
|       *.sublime-package
|       
+---Lib --> libs required by Packages
|   +---python33
|   \---python38
|               
+---Local
|       Auto Save Session.sublime_session
|       Backup Auto Save Session.sublime_session
|       Backup Session.sublime_session
|       License.sublime_license
|       Session.sublime_session --> contains project history, edit with different editor to clean up.
|       
\---Packages --> loose and source code, not from Package Control
    |   
    +---Default --> TODO
    |       Context.sublime-menu
    |       Side Bar.sublime-menu
    |       
    +---example_plugin --> our example
    |   |   .gitattributes
    |   |   .gitignore
    |   |   .python-version
    |   |   basic_source.py
    |   |   Default.sublime-commands
    |   |   LICENSE
    |   |   Main.sublime-menu
    |   |   more_source.py
    |   |   example_plugin.sublime-settings
    |   |   README.md
    |   |   
    |   \---test
    |           some_test_code.py
    |           
    \---User --> 
            *.sublime-settings
            Context.sublime-menu
            Main.sublime-menu
            Side Bar.sublime-menu
            Tab Context.sublime-menu
            CT.sublime-color-scheme
            Default (Windows).sublime-keymap
            Default.sublime-commands
```

TODO May also have stuff like:
- *.tmLanguage
- *.sublime-syntax
- *.sublime-color-scheme
- *.sublime-keymap
- dependencies.json
- messages.json
