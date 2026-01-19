# silly wrapper around git so we can ignore ~/.gitconfig as needed

import os
import subprocess


def call(args, gitconfig=False, foreground=False, cwd=None):
    if gitconfig:
        bcmd = ["git"]
    else:
        # still use the rest of the environment
        env = os.environ.copy()
        env["GIT_CONFIG_GLOBAL"] = "/dev/null"
        env["GIT_CONFIG_SYSTEM"] = "/dev/null"
        bcmd = ["git"]

    ret = subprocess.run(bcmd + args, capture_output=not foreground, cwd=cwd)

    if ret.returncode != 0:
        return None

    return True if foreground else ret.stdout
