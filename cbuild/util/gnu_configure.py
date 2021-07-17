from cbuild.core import logger, paths, profile
from cbuild.util import make
from cbuild import cpu

import re
import shutil
import shlex

benv = {
    "lt_cv_sys_lib_dlsearch_path_spec": \
        "/usr/lib64 /usr/lib32 /usr/lib /lib /usr/local/lib"
}

def _cache_expand(s, eenv):
    if len(s) == 0 or s[0] != "$":
        return s

    if not s.startswith("${") or not s.endswith("}"):
        logger.get().log(f"Malformed autoconf cache entry: {s}")
        return None

    v = s[2:-1].split("=")
    if len(v) != 2:
        logger.get().log(f"Malformed autoconf cache entry: {s}")
        return None

    if v[0] in eenv:
        return eenv[v[0]]

    v = v[1]
    if v.startswith("'") or v.startswith("\""):
        vs = shlex.split(v)
        if len(vs) != 1:
            logger.get().log(f"Invalid cache entry value: {v}")
            return None
        return vs[0]

    return v

def _read_cache(cpath, cname, eenv):
    with open(cpath / cname) as f:
        for ln in f.readlines():
            ln = ln.strip()
            if len(ln) == 0 or ln[0] == "#":
                continue
            pos = ln.find("=")
            if pos >= 0:
                cv = _cache_expand(ln[pos + 1:], eenv)
                if cv:
                    eenv[ln[0:pos]] = cv
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
            "x86_64*",  ["x86_64-linux"],
            "ppc64*",   ["powerpc-common", "powerpc-linux", "powerpc64-linux"],
            "*", []
        )
        for l in cl:
            _read_cache(cachedir, l, eenv)
    else:
        _read_cache(cachedir, "musl-linux", eenv)

    eenv.update(env)

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
