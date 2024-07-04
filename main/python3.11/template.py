pkgname = "python3.11"
_majver = "3.11"
pkgver = f"{_majver}.9"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--enable-ipv6",
    "--enable-loadable-sqlite-extensions",
    "--with-computed-gotos",
    "--with-system-ffi",
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
    "zlib-ng-compat-devel",
]
checkdepends = ["ca-certificates"]
depends = ["ca-certificates"]
pkgdesc = "Python programming language (3.11)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://python.org"
source = f"https://python.org/ftp/python/{pkgver}/Python-{pkgver}.tar.xz"
sha256 = "9b1e896523fc510691126c864406d9360a3d1e986acbda59cda57b5abda45b87"
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
    hostmakedepends += [f"python{_majver}"]
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


def pre_configure(self):
    self.rm("Modules/_ctypes/darwin", recursive=True)
    self.rm("Modules/_ctypes/libffi_osx", recursive=True)


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
    self.uninstall(f"{lbase}/lib2to3/tests")
    self.uninstall(f"{lbase}/turtle.py")

    self.rename(
        f"{lbase}/config*/libpython*.a",
        "usr/lib",
        glob=True,
        keep_name=True,
        relative=False,
    )

    # nuke stuff that conflicts with primary python package
    self.uninstall("usr/bin/pydoc3")
    self.uninstall("usr/bin/python3")
    self.uninstall("usr/bin/python3-config")
    self.uninstall("usr/lib/libpython3.so")
    self.uninstall("usr/lib/pkgconfig/python3.pc")
    self.uninstall("usr/lib/pkgconfig/python3-embed.pc")
    self.uninstall("usr/share/man/man1/python3.1")


@subpackage("python3.11-devel")
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
