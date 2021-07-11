from cbuild.core import paths
from cbuild.util import make

import re
import shutil

benv = {
    "lt_cv_sys_lib_dlsearch_path_spec": \
        "/usr/lib64 /usr/lib32 /usr/lib /lib /usr/local/lib"
}

def configure(
    pkg, configure_dir = None, configure_script = "configure",
    build_dir = "build", extra_args = [], env = {}
):
    if configure_dir:
        cscript = str(pkg.chroot_wrksrc / configure_dir / configure_script)
        rscript = pkg.abs_wrksrc / configure_dir / configure_script
    else:
        cscript = str(pkg.chroot_wrksrc / configure_script)
        rscript = pkg.abs_wrksrc / configure_script

    (pkg.abs_build_wrksrc / build_dir).mkdir(parents = True, exist_ok = True)

    mdir = str(paths.masterdir())
    cargs = []

    cargs = [
        "--prefix=/usr", "--sysconfdir=/etc", "--sbindir=/usr/bin",
        "--bindir=/usr/bin", "--mandir=/usr/share/man",
        "--infodir=/usr/share/info", "--localstatedir=/var"
    ]

    if pkg.triplet:
        cargs.append("--build=" + pkg.triplet)
        cargs.append("--host=" + pkg.triplet)

    # autoconf cache
    eenv = dict(benv)
    eenv.update(env)
    cachedir = paths.cbuild() / "misc/autoconf_cache"
    with open(cachedir / "musl-linux") as f:
        for ln in f.readlines():
            ln = ln.strip()
            if len(ln) == 0 or ln[0] == "#":
                continue
            pos = ln.find("=")
            if pos >= 0:
                eenv[ln[0:pos]] = ln[pos + 1:]
            else:
                eenv[ln] = "yes"

    # http://lists.gnu.org/archive/html/libtool-patches/2004-06/msg00002.html
    with open(rscript) as f:
        with open(rscript.with_suffix(".tmp"), "w") as tf:
            for ln in f:
                tf.write(re.sub(
                    r"^([ \t]*tmp_sharedflag)='-shared'",
                    r"\1='-shared -Wl,--as-needed'", ln
                ))

    rscript.unlink()
    rscript.with_suffix(".tmp").rename(rscript)
    rscript.chmod(0o755)

    pkg.do(
        cscript, cargs + pkg.configure_args + extra_args,
        wrksrc = build_dir, build = True, env = eenv
    )

def get_make_env():
    return benv

def replace_guess(pkg):
    for f in pkg.abs_wrksrc.rglob("*config*.*"):
        if f.is_symlink():
            continue
        if f.suffix == ".guess":
            f.unlink()
            shutil.copy(paths.cbuild() / "misc/config.guess", f)
        elif f.suffix == ".sub":
            f.unlink()
            shutil.copy(paths.cbuild() / "misc/config.sub", f)
