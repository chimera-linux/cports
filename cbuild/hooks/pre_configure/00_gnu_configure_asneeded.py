import os
from os import path
import re

def invoke(pkg):
    if not pkg.build_style or pkg.build_style != "gnu_configure":
        return

    confp = pkg.abs_wrksrc / "configure"

    if not path.isfile(confp):
        return

    # http://lists.gnu.org/archive/html/libtool-patches/2004-06/msg00002.html
    with open(confp) as f:
        with open(str(confp) + ".tmp", "w") as tf:
            for ln in f:
                tf.write(re.sub(
                    r"^([ \t]*tmp_sharedflag)='-shared'",
                    r"\1='-shared -Wl,--as-needed'", ln
                ))

    os.unlink(confp)
    os.rename(str(confp) + ".tmp", confp)
    os.chmod(confp, 0o755)
