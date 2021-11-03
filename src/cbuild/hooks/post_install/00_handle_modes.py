# this runs early so that proper permissions can get applied
# otherwise we would not get validation by e.g. the suid scanner

def invoke(pkg):
    for k in pkg.file_modes:
        p = pkg.destdir / k

        if not p.exists():
            pkg.error(f"non-existent file in file_modes: {k}")

        if len(pkg.file_modes[k]) != 3:
            pkg.error(f"invalid file_modes value for {k}")

        uname, gname, fmode = pkg.file_modes[k]

        def _validate_name(n):
            # skip
            if n is None:
                return
            # check if a valid string
            if not isinstance(n, str):
                pkg.error("file_modes owner/group value must be a string")
            # valid format
            col = n.find(":")
            if col <= 0 or len(n[col + 1:]) == 0:
                pkg.error("file_modes owner/group value has invalid format")
            # uid/gid converts to an integer
            mint = True
            try:
                int(n[col + 1:])
            except ValueError:
                mint = False
            if not mint:
                pkg.error("file_modes owner/group must have a numeric ID")

        _validate_name(uname)
        _validate_name(gname)

        if not isinstance(fmode, int):
            pkg.error("file_modes mode must be an integer")

        p.chmod(fmode)
