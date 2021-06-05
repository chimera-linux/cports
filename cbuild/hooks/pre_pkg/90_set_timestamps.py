from datetime import datetime
import os

def invoke(pkg):
    if not pkg.rparent.source_date_epoch:
        return

    ts = pkg.rparent.source_date_epoch
    dt = datetime.fromtimestamp(ts).ctime()

    pkg.log(f"setting mtimes to {dt}")

    for root, dirs, files in os.walk(pkg.destdir):
        for f in files:
            os.utime(os.path.join(root, f), (ts, ts), follow_symlinks = False)
