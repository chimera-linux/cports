import re

def invoke(pkg):
    if not pkg.build_style or pkg.build_style != "gnu_configure":
        return

    confp = pkg.abs_wrksrc / "configure"

    if not confp.is_file():
        return

    # http://lists.gnu.org/archive/html/libtool-patches/2004-06/msg00002.html
    with open(confp) as f:
        with open(str(confp) + ".tmp", "w") as tf:
            for ln in f:
                tf.write(re.sub(
                    r"^([ \t]*tmp_sharedflag)='-shared'",
                    r"\1='-shared -Wl,--as-needed'", ln
                ))

    confp.unlink()
    confp.with_suffix(".tmp").rename(confp)
    confp.chmod(0o755)
