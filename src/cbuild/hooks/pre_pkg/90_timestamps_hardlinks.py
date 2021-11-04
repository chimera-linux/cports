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
    if not pkg.rparent.source_date_epoch:
        return

    ts = pkg.rparent.source_date_epoch
    dt = datetime.fromtimestamp(ts).ctime()

    pkg.log(f"detecting hardlinks and setting mtimes to {dt}")

    # mappings from inode to full path
    hards = {}
    for root, dirs, files in os.walk(pkg.destdir):
        for f in files:
            absp = os.path.join(root, f)
            st = os.lstat(absp)
            if st.st_nlink > 1:
                if not st.st_ino in hards:
                    # first occurence
                    hards[st.st_ino] = absp
                else:
                    p1 = os.path.relpath(absp, pkg.destdir)
                    p2 = os.path.relpath(hards[st.st_ino], pkg.destdir)
                    pkg.error(f"hardlink detected ({p1}, previously {p2})")
            # update timestamp
            os.utime(absp, (ts, ts), follow_symlinks = False)
