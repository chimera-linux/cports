# sets the timestamps for reproducibility

from datetime import datetime
import os


def invoke(pkg):
    if not pkg.rparent.source_date_epoch:
        return

    ts = pkg.rparent.source_date_epoch
    dt = datetime.fromtimestamp(ts).ctime()

    pkg.logger.out_plain(f"  \f[blue]mtime:\f[] {dt}")

    for root, dirs, files in os.walk(pkg.destdir):
        for d in dirs:
            absp = os.path.join(root, d)
            # update timestamp
            os.utime(absp, (ts, ts), follow_symlinks=False)

        for f in files:
            absp = os.path.join(root, f)
            # update timestamp
            os.utime(absp, (ts, ts), follow_symlinks=False)
