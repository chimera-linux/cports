# detects and errors on hardlinks
#
# if something needs hardlinks in the future, we should
# make it an option and update the apk generator to preserve
# the hardlinks so they do not get made into multiple files

import os


def invoke(pkg):
    if pkg.options["hardlinks"]:
        return

    # mappings from inode to full path
    hards = {}
    harderr = False
    for root, dirs, files in os.walk(pkg.destdir):
        for f in files:
            absp = os.path.join(root, f)
            st = os.lstat(absp)
            if st.st_nlink > 1:
                if st.st_ino not in hards:
                    # first occurence
                    hards[st.st_ino] = absp
                else:
                    p1 = os.path.relpath(absp, pkg.destdir)
                    p2 = os.path.relpath(hards[st.st_ino], pkg.destdir)
                    pkg.log_red(f"hardlink detected ({p1}, previously {p2})")
                    harderr = True

    if harderr:
        pkg.error("hardlinks were found, cannot proceed")
