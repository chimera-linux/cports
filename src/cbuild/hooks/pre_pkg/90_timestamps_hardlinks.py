# sets the timestamps for reproducibility
#
# also detects and errors on hardlinks
#
# if something needs hardlinks in the future, we should
# make it an option and update the apk generator to preserve
# the hardlinks so they do not get made into multiple files

from datetime import datetime
import os

def invoke(pkg):
    hardlinks = pkg.options["hardlinks"]

    if not pkg.rparent.source_date_epoch and hardlinks:
        return

    ts = pkg.rparent.source_date_epoch
    dt = None
    if ts:
        dt = datetime.fromtimestamp(ts).ctime()

    if ts and not hardlinks:
        pkg.log(f"detecting hardlinks and setting mtimes to {dt}")
    elif ts:
        pkg.log(f"setting mtimes to {dt}")
    else:
        pkg.log(f"detecting hardlinks")

    # mappings from inode to full path
    hards = {}
    for root, dirs, files in os.walk(pkg.destdir):
        for f in files:
            absp = os.path.join(root, f)
            st = os.lstat(absp)
            if st.st_nlink > 1 and not hardlinks:
                if not st.st_ino in hards:
                    # first occurence
                    hards[st.st_ino] = absp
                else:
                    p1 = os.path.relpath(absp, pkg.destdir)
                    p2 = os.path.relpath(hards[st.st_ino], pkg.destdir)
                    pkg.error(f"hardlink detected ({p1}, previously {p2})")
            # update timestamp
            if ts:
                os.utime(absp, (ts, ts), follow_symlinks = False)
