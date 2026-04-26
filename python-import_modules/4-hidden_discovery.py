#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names in the module
    names = dir(hidden_4)
    # Sort names alphabetically
    names.sort()

    for name in names:
        # Check if the name does NOT start with __
        if not name.startswith("__"):
            print("{}".format(name))
