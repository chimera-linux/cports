from cbuild.core import paths, profile
from cbuild.util import make
from cbuild import cpu

import re
import shutil

benv = {
    "lt_cv_sys_lib_dlsearch_path_spec": \
        "/usr/lib64 /usr/lib32 /usr/lib /lib /usr/local/lib"
}

def _read_cache(cpath, cname, eenv):
    with open(cpath / cname) as f:
        for ln in f.readlines():
            ln = ln.strip()
            if len(ln) == 0 or ln[0] == "#":
                continue
            pos = ln.find("=")
            if pos >= 0:
                eenv[ln[0:pos]] = ln[pos + 1:]
            else:
                eenv[ln] = "yes"

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

    # autoconf cache
    eenv = dict(benv)
    eenv.update(env)

    # caches taken from openembedded
    cachedir = paths.cbuild() / "misc/autoconf_cache"

    if pkg.build_profile.triplet:
        cargs.append("--build=" + profile.get_profile(cpu.host()).short_triplet)
        cargs.append("--host=" + pkg.build_profile.short_triplet)

    if pkg.build_profile.cross:
        cargs.append("--with-sysroot=" + str(pkg.build_profile.sysroot))
        cargs.append("--with-libtool-sysroot=" + str(pkg.build_profile.sysroot))
        # base cache
        _read_cache(cachedir, "common-linux", eenv)
        _read_cache(cachedir, "musl-linux", eenv)
        # endian cache
        _read_cache(cachedir, "endian-" + pkg.build_profile.endian, eenv)
        # machine cache
        cl = cpu.match_arch(
            pkg.build_profile.arch,
            "arm*",     ["arm-common", "arm-linux"],
            "aarch64*", ["aarch64-linux"],
            "i686*",    ["ix86-common"],
            "mips*",    ["mips-common", "mips-linux"],
            "x86_64*",  ["x86_64-linux"],
            "ppc64*",   ["powerpc-common", "powerpc-linux", "powerpc64-linux"],
            "ppc*",     ["powerpc-common", "powerpc-linux", "powerpc32-linux"],
            "*", []
        )
        for l in cl:
            _read_cache(cachedir, l, eenv)
    else:
        _read_cache(cachedir, "musl-linux", eenv)

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
