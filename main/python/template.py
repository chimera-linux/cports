pkgname = "python"
pkgver = "3.14.5"
_majver = pkgver[: pkgver.rfind(".")]
pkgrel = 0
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
    + "-i test_tools "
    + "-i test_timeout "  # ??? env changed
    + "-i test_functools "  # ppc64le stack overflow
    + "-i test_isinstance "  # ppc64le stack overflow
    + "-i test_pickle "  # ppc64le stack overflow
    + "-i test_pickletools "  # ppc64le stack overflow
    + "-i test_pgo_exclude "  # seems harmless?
    + "-i test_bang_completion_without_do_shell "  # dislikes our libedit
    + "-i test.test_strptime.StrptimeTests.test_date_locale2 "
    # these need net
    + "-i test_urllib2 "
    + "-i test_urllibnet "
    + "-i test_urllib2net "
]
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "pkgconf",
]
makedepends = [
    "bluez-headers",
    "bzip2-devel",
    "libedit-devel",
    "libexpat-devel",
    "libffi8-devel",
    "linux-headers",
    "openssl3-devel",
    "sqlite-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["ca-certificates"]
depends = [self.with_pkgver("python-meta"), "ca-certificates"]
provides = [self.with_pkgver(f"python{_majver}")]
install_if = [self.with_pkgver("python-meta")]
pkgdesc = "Python programming language"
license = "Python-2.0"
url = "https://python.org"
source = f"https://python.org/ftp/python/{pkgver}/Python-{pkgver}.tar.xz"
sha256 = "7e32597b99e5d9a39abed35de4693fa169df3e5850d4c334337ffd6a19a36db6"
# use a chunky stack; python by default does not use more than 1 thread
# but anything dlopened from it will be stuck with the default stacksize
# (e.g. python gtk programs, gtk loads icons from a threadpool and it may
# result in librsvg rust stack overflowing) so assume a bigger default
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
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

_has_tail = True

match self.profile().arch:
    case "ppc" | "ppc64" | "ppc64le":
        _has_tail = False


def init_configure(self):
    if not self.profile().cross and self.has_lto():
        self.configure_args += ["--enable-optimizations"]
        if _has_tail:
            self.configure_args += ["--with-tail-call-interp"]
    bigend = "yes" if (self.profile().endian == "big") else "no"
    self.configure_args.append("ax_cv_c_float_words_bigendian=" + bigend)
    # real configure and linker flags here
    self.env["CFLAGS_NODIST"] = self.get_cflags(shell=True)
    self.env["LDFLAGS_NODIST"] = self.get_ldflags(shell=True)
    # python is being bootstrapped, so set it here (the hook won't set it)
    self.python_version = _majver


def install(self):
    self.make.invoke(
        ["install", "maninstall"], ["DESTDIR=" + str(self.chroot_destdir)]
    )
    self.install_license("LICENSE")

    self.uninstall("usr/bin/idle*", glob=True)

    lbase = "usr/lib/python" + _majver

    self.uninstall(f"{lbase}/idlelib")
    self.uninstall(f"{lbase}/tkinter")
    self.uninstall(f"{lbase}/turtledemo")
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
def _(self):
    self.depends = [self.parent]

    def install():
        self.take("cmd:python*-config")
        self.take("lib:*.a")
        self.take("usr/lib/pkgconfig")
        for f in (
            self.parent.destdir / f"usr/include/python{_majver}"
        ).iterdir():
            if f.name == "pyconfig.h":
                continue
            self.take(str(f.relative_to(self.parent.destdir)))

    return install


@subpackage("python-tests")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "test module"

    return ["usr/lib/python*/test"]


@subpackage("python-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    self.provides = [
        self.with_pkgver(f"base-python{_majver}"),
        self.with_pkgver(f"python-python{_majver}-meta"),
    ]

    return []
