# update pyver in autosplit logic and pre_pkg hook on major bumps
pkgname = "python"
_majver = "3.12"
pkgver = f"{_majver}.4"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--enable-ipv6",
    "--enable-loadable-sqlite-extensions",
    "--enable-shared",
    "--with-computed-gotos",
    "--with-readline=editline",
    "--with-system-expat",
    "--without-ensurepip",
]
# bmake has broken cross build (unsupported stuff in PYTHON_FOR_BUILD)
make_cmd = "gmake"
make_check_target = "quicktest"
# disable tests that disagree with our build environment or musl
make_check_args = [
    "EXTRATESTOPTS="
    + "-i test_chown_* "
    + "-i test_getspnam_exception "
    + "-i test_find_library_with_* "
    + "-i test_localtime_daylight_*_dst_true "
    + "-i test__locale "
    + "-i test_c_locale_coercion "
    + "-i test_cmd_line "
    + "-i test_locale "
    + "-i test_os "
    + "-i test_re "
    + "-i test_readline "
    + "-i test_threading "
    + "-i test_unicodedata "
    + "-i test_urllib2net "  # just loops blocked connection failures into success
    + "-i test_tools "
    + "-i test_functools "  # ppc64le stack overflow
    + "-i test_isinstance "  # ppc64le stack overflow
]
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "pkgconf",
    "gmake",
]
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
    "zlib-ng-compat-devel",
]
checkdepends = ["ca-certificates"]
depends = [self.with_pkgver(f"base-python{_majver}"), "ca-certificates"]
provides = [self.with_pkgver(f"python{_majver}")]
install_if = [self.with_pkgver(f"base-python{_majver}")]
pkgdesc = "Python programming language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://python.org"
source = f"https://python.org/ftp/python/{pkgver}/Python-{pkgver}.tar.xz"
sha256 = "f6d419a6d8743ab26700801b4908d26d97e8b986e14f95de31b32de2b0e79554"
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

    self.uninstall("usr/bin/2to3")
    self.uninstall("usr/bin/idle*", glob=True)

    lbase = "usr/lib/python" + _majver

    self.uninstall(f"{lbase}/idlelib")
    self.uninstall(f"{lbase}/tkinter")
    self.uninstall(f"{lbase}/turtledemo")
    self.uninstall(f"{lbase}/test")
    self.uninstall(f"{lbase}/turtle.py")

    self.rename(
        f"{lbase}/config*/libpython*.a",
        "usr/lib",
        glob=True,
        keep_name=True,
        relative=False,
    )

    self.install_file(
        self.files_path / "EXTERNALLY-MANAGED", f"usr/lib/python{_majver}"
    )

    self.install_link("usr/bin/pydoc", "pydoc" + _majver)
    self.install_link("usr/bin/python", "python" + _majver)
    self.install_link("usr/share/man/man1/python.1", "python" + _majver + ".1")


@subpackage("python-devel")
def _devel(self):
    self.depends = [self.parent]

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
    self.subdesc = "recommends package"
    self.options = ["empty"]

    return []
