from util.supporting.settings import log


def check_string_length(func):
    """
    A decorator that checks the length of a string returned by a function.
    If the length of the string is greater than 8191 characters, a ValueError is raised.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        new_lines_count = result.count("\n")

        if new_lines_count > 1:
            for line in result.splitlines():
                if len(line) > 8191:
                    log.warning(f"String length of {len(line)} is greater than 4000 characters.")
        else:
            if len(result) > 8191:
                raise ValueError(f"String length of {len(result)} is greater than 4000 characters.")

        return result

    return wrapper
