# update pyver in autosplit logic and pre_pkg hook on major bumps
pkgname = "python"
_majver = "3.12"
pkgver = f"{_majver}.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--enable-ipv6",
    "--enable-loadable-sqlite-extensions",
    "--with-computed-gotos",
    "--with-system-expat",
    "--with-readline=editline",
    "--without-ensurepip",
]
configure_gen = []
# bmake has broken cross build (unsupported stuff in PYTHON_FOR_BUILD)
make_cmd = "gmake"
make_check_target = "quicktest"
# disable tests that disagree with our build environment or musl
make_check_args = [
    "EXTRATESTOPTS="
    "-i test_chown_* "
    "-i test_getspnam_exception "
    "-i test_find_library_with_* "
    "-i test_localtime_daylight_*_dst_true "
    "-i test__locale "
    "-i test_c_locale_coercion "
    "-i test_cmd_line "
    "-i test_locale "
    "-i test_os "
    "-i test_re "
    "-i test_readline "
    "-i test_threading "
    "-i test_unicodedata "
    "-i test_urllib2net "  # just loops blocked connection failures into success
    "-i test_tools "
]
hostmakedepends = ["pkgconf", "gmake"]
makedepends = [
    "bluez-headers",
    "bzip2-devel",
    "libedit-devel",
    "libexpat-devel",
    "libffi-devel",
    "linux-headers",
    "openssl-devel",
    "sqlite-devel",
    "xz-devel",
    "zlib-devel",
]
checkdepends = ["ca-certificates"]
depends = [f"base-python{_majver}={pkgver}-r{pkgrel}", "ca-certificates"]
provides = [f"python{_majver}={pkgver}-r{pkgrel}"]
install_if = [f"base-python{_majver}={pkgver}-r{pkgrel}"]
pkgdesc = "Python programming language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://python.org"
source = f"https://python.org/ftp/python/{pkgver}/Python-{pkgver}.tar.xz"
sha256 = "be28112dac813d2053545c14bf13a16401a21877f1a69eb6ea5d84c4a0f3d870"
# FIXME int cfi; cfi ftbfs, int fails ctypes test
# we cannot enable ubsan stuff because there is known UB where tests
# are just skipped and so on, so be on the safe side for the time being
hardening = ["vis", "!cfi", "!int"]

env = {
    # emulate python's configure stuff but with -O2
    "OPT": "-g -fwrapv -O2 -Wall",
    "CFLAGS_ALIASING": "-fno-strict-aliasing",
    # we pass them via NODIST so they do not propagate to modules
    "CFLAGS": "",
    "LDFLAGS": "",
}

if self.profile().cross:
    hostmakedepends += ["python"]
    configure_args += [f"--with-build-python=python{_majver}"]


def init_configure(self):
    if not self.profile().cross and self.has_lto():
        self.configure_args.append("--enable-optimizations")
    bigend = "yes" if (self.profile().endian == "big") else "no"
    self.configure_args.append("ax_cv_c_float_words_bigendian=" + bigend)
    # real configure and linker flags here
    self.env["CFLAGS_NODIST"] = self.get_cflags(shell=True)
    self.env["LDFLAGS_NODIST"] = self.get_ldflags(shell=True)
    # python is being bootstrapped, so set it here (the hook won't set it)
    self.python_version = _majver


def do_install(self):
    self.make.invoke(
        ["install", "maninstall"], ["DESTDIR=" + str(self.chroot_destdir)]
    )
    self.install_license("LICENSE")

    self.rm(self.destdir / "usr/bin/2to3", force=True)
    for f in (self.destdir / "usr/bin").glob("idle*"):
        f.unlink()

    lbase = self.destdir / ("usr/lib/python" + _majver)

    self.rm(lbase / "idlelib", recursive=True)
    self.rm(lbase / "tkinter", recursive=True)
    self.rm(lbase / "turtledemo", recursive=True)
    self.rm(lbase / "test", recursive=True)

    (lbase / "turtle.py").unlink(missing_ok=True)

    for f in lbase.glob("config-*"):
        for ff in f.glob("libpython*.a"):
            self.mv(ff, self.destdir / "usr/lib")

    self.install_file(
        self.files_path / "EXTERNALLY-MANAGED", f"usr/lib/python{_majver}"
    )

    self.install_link("pydoc" + _majver, "usr/bin/pydoc")
    self.install_link("python" + _majver, "usr/bin/python")
    self.install_link("python" + _majver + ".1", "usr/share/man/man1/python.1")


@subpackage("python-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    def install():
        import os

        self.take("usr/bin/python*-config")
        self.take("usr/lib/pkgconfig")
        self.take("usr/lib/*.a")
        self.take("usr/include")
        pypath = "usr/include/python" + _majver
        os.makedirs(self.parent.destdir / pypath)
        os.rename(
            self.destdir / pypath / "pyconfig.h",
            self.parent.destdir / pypath / "pyconfig.h",
        )

    return install


@subpackage(f"base-python{_majver}")
def _ver(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.options = ["empty"]

    return []
