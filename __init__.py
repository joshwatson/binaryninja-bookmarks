'''
bookmarks.py - Create/List bookmarks in Binary Ninja

Copyright (c) 2016 Josh Watson

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
'''
from collections import OrderedDict

import binaryninja as bn


def create_bookmark(view, address):
    try:
        bookmarks = view.query_metadata('bookmarks')
    except KeyError:
        bookmarks = OrderedDict()
        view.store_metadata('bookmarks', bookmarks)

    bookmark_name = bn.get_text_line_input(
        "Create new bookmark", "Enter bookmark name:"
    )
    if bookmark_name:
        bookmarks[address] = bookmark_name
        view.store_metadata("bookmarks", bookmarks)


def goto_bookmark(view):
    try:
        bookmarks = view.query_metadata('bookmarks')
    except KeyError:
        bookmarks = OrderedDict()
        view.store_metadata('bookmarks', bookmarks)

    if not bookmarks:
        bn.show_message_box(
            'Bookmark error', 'There are no bookmarks yet.',
            icon=bn.enums.MessageBoxIcon.ErrorIcon
        )
        return

    # Metadata can only store string keys in dictionaries currently.
    # Therefore, we have to convert keys to integers.
    chosen_bookmark = bn.get_choice_input(
        'Go to bookmark', 'Bookmarks:',
        ['0x{:x} {}'.format(int(addr), bookmark)
         for addr, bookmark in bookmarks.iteritems()]
    )

    # Again, we hae to convert string keys to integers.
    if chosen_bookmark is not None:
        navigate_to = int(bookmarks.keys()[chosen_bookmark])

        view.file.navigate(view.file.view, navigate_to)


bn.PluginCommand.register_for_address(
    'Create Bookmark', 'Create a bookmark at this address.', create_bookmark
)
bn.PluginCommand.register('Go to Bookmark', 'Go to a bookmark.', goto_bookmark)