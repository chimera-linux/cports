# this runs early so that proper permissions can get applied
# otherwise we would not get validation by e.g. the suid scanner

import os


def invoke(pkg):
    # require files with security xattrs to have an explicit mode, just to
    # make sure the packager knows what it is; suid files are checked later
    # after all the modes are applied (suid files without file_mode are not
    # allowed)
    for k in pkg.file_xattrs:
        if k in pkg.file_modes:
            continue
        for xa in pkg.file_xattrs[k]:
            if xa.startswith("security."):
                pkg.error(
                    f"security xattr without an explicit mode: {k}",
                    hint="specify mode for the file in 'file_modes'",
                )

    for k in pkg.file_modes:
        # mkdirs, done later but still validated
        isdir = k.startswith("+")

        p = pkg.destdir / k

        if not isdir and not p.exists():
            pkg.error(f"non-existent file in file_modes: {k}")

        fml = len(pkg.file_modes[k])
        if fml != 3 and fml != 4:
            pkg.error(
                f"invalid file_modes value for {k}",
                hint="it must be a 3-tuple or a 4-tuple",
            )

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

        if isdir:
            continue

        if recursive:
            for root, dirs, files in os.walk(p):
                for d in dirs:
                    os.chmod(d, fmode)
                for f in files:
                    os.chmod(f, fmode)
        else:
            os.chmod(p, fmode)
