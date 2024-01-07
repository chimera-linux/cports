# this runs early so that proper permissions can get applied
# otherwise we would not get validation by e.g. the suid scanner

import os


def invoke(pkg):
    for k in pkg.file_modes:
        p = pkg.destdir / k

        if not p.exists():
            pkg.error(f"non-existent file in file_modes: {k}")

        if len(pkg.file_modes[k]) != 3:
            pkg.error(f"invalid file_modes value for {k}")

        recursive = False
        if len(pkg.file_modes[k]) == 4:
            uname, gname, fmode, recursive = pkg.file_modes[k]
        else:
            uname, gname, fmode = pkg.file_modes[k]

        if not isinstance(uname, str):
            pkg.error("file_modes owner value must be a user name")
        if not isinstance(uname, str):
            pkg.error("file_modes group value must be a group name")
        if not isinstance(fmode, int):
            pkg.error("file_modes mode must be an integer")
        if not isinstance(recursive, bool):
            pkg.error("file_mods recursive flag must be a boolean")

        if recursive:
            for root, dirs, files in os.walk(p):
                for d in dirs:
                    os.chmod(d, fmode)
                for f in files:
                    os.chmod(f, fmode)
        else:
            os.chmod(p, fmode)
