# Bookmarks (v0.1b)
Author: **Josh Watson**

_A plugin that adds bookmarking functionality._

## Description:

This plugin enables a Binary Ninja user to bookmark addresses of interest and quickly navigate back to them at a later time. As the API for loading and saving user data to the analysis database is not available yet, the bookmarks must be manually saved and loaded to a separate file for now.

To install this plugin, navigate to your Binary Ninja plugins directory, and run

```git clone https://github.com/joshwatson/binaryninja-bookmarks.git bookmarks```

Then create a python file called `bookmarks.py` with the contents

```import bookmarks```

## Minimum Version

This plugin requires the following minimum version of Binary Ninja:

 * dev (Personal) - 1.0.dev-71
 * dev (Commercial) - 1.0.dev-71
 * release (Commercial) - 1.0.7
 * release (Personal) - 1.0.7



## License

This plugin is released under a [MIT](LICENSE) license.


