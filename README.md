# TermMenu

This is a little Python project that I wanted to do for some time.

The idea is that you should be able to make a terminal menu (below) easily and compactly.

```text
Choose one:
1. Start game
2. Settings
3. And more
> {User input here}
```

## Documentation

Read the documentation on [ReadTheDocs](https://pytermmenu.readthedocs.io/en/latest/index.html).

## Usage

To start off you need to import the library, and create a new menu.

```py
import termmenu

testmenu = termmenu.Menu(title="What's up") # title is optional
```

### Adding entries

To add entries, we use `Menu.add_entry`, usage:

```py
Menu.add_entry(text, run=None, entry=None)
```