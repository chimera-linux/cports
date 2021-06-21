pkgname = "python"
_majver = "3.9"
version = f"{_majver}.5"
revision = 1
wrksrc = f"Python-{version}"
hostmakedepends = ["pkgconf"]
# FIXME: expat, readline, sqlite
makedepends = [
    "libffi-devel", "openssl-devel", "bzip2-devel",
    "zlib-devel", "liblzma-devel"
]
depends = ["ca-certificates"]
short_desc = "Python programming language"
maintainer = "q66 <daniel@octaforge.org>"
license = "Python-2.0"
homepage = "https://python.org"
distfiles = [f"https://python.org/ftp/python/{version}/Python-{version}.tar.xz"]
checksum = ["0c5a140665436ec3dbfbb79e2dfb6d192655f26ef4a29aeffcb6d1820d716d83"]

def pre_configure(self):
    import shutil
    shutil.rmtree(
        self.abs_wrksrc / "Modules/_ctypes/darwin", ignore_errors = True
    )
    shutil.rmtree(
        self.abs_wrksrc / "Modules/_ctypes/libffi_osx", ignore_errors = True
    )

def do_configure(self):
    from cbuild import cpu
    bigend = "yes" if (cpu.target_endian() == "big") else "no"
    self.do(self.chroot_wrksrc / "configure", self.configure_args + [
        "--enable-shared", "--enable-ipv6", "--with-computed-gotos",
        "--with-system-ffi", "--without-ensurepip",
        "ax_cv_c_float_words_bigendian=" + bigend
    ])

def init_build(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.build()

def do_install(self):
    import shutil

    self.make.invoke(
        ["install", "maninstall"], ["DESTDIR=" + str(self.chroot_destdir)]
    )
    self.install_license("LICENSE")

    (self.destdir / "usr/bin/2to3").unlink(missing_ok = True)
    for f in (self.destdir / "usr/bin").glob("idle*"):
        f.unlink()

    lbase = self.destdir / ("usr/lib/python" + _majver)

    shutil.rmtree(lbase / "idlelib", ignore_errors = True)
    shutil.rmtree(lbase / "tkinter", ignore_errors = True)
    shutil.rmtree(lbase / "turtledemo", ignore_errors = True)
    shutil.rmtree(lbase / "test", ignore_errors = True)
    shutil.rmtree(lbase / "lib2to3/tests", ignore_errors = True)

    (lbase / "turtle.py").unlink(missing_ok = True)

    # remove references to the install(1) wrapper
    def subst_wdir(f):
        import os
        if not f.is_file():
            return
        with open(f) as ifile:
            with open(f.with_suffix(".new"), "w") as ofile:
                for ln in ifile:
                    ln = ln.replace(
                        self.env["CBUILD_STATEDIR"] + "/wrappers", "/usr/bin"
                    )
                    ofile.write(ln)
        os.rename(f.with_suffix(".new"), f)

    for f in lbase.glob("_sysconfigdata_*_*.py"):
        subst_wdir(f)
    for f in lbase.glob("config-*"):
        subst_wdir(f / "Makefile")
        for ff in f.glob("libpython*.a"):
            shutil.move(ff, self.destdir / "usr/lib")

    self.install_link("pydoc" + _majver, "usr/bin/pydoc")
    self.install_link("python" + _majver, "usr/bin/python")
    self.install_link("python" + _majver + ".1", "usr/share/man/man1/python.1")

@subpackage("python-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"{pkgname}={version}-r{revision}"]

    def install():
        import os
        self.take("usr/bin/python*-config")
        self.take("usr/lib/pkgconfig")
        self.take("usr/include")
        self.take("usr/lib/*.a")
        pypath = "usr/include/python" + _majver
        os.makedirs(self.parent.destdir / pypath)
        os.rename(
            self.destdir / pypath / "pyconfig.h",
            self.parent.destdir / pypath / "pyconfig.h"
        )

    return install
