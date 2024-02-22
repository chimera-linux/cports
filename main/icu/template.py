pkgname = "icu"
pkgver = "74.2"  # change path in build.patch when updating
pkgrel = 0
build_wrksrc = "source"
build_style = "gnu_configure"
configure_args = [
    "--with-data-packaging=archive",
    "--enable-static",
]
make_cmd = "gmake"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gmake",
    "pkgconf",
]
checkdepends = ["python"]
pkgdesc = "Robust and fully-featured Unicode libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ICU"
url = "https://home.unicode.org"
source = f"https://github.com/unicode-org/{pkgname}/releases/download/release-{pkgver.replace('.', '-')}/icu4c-{pkgver.replace('.', '_')}-src.tgz"
sha256 = "68db082212a96d6f53e35d60f47d38b962e9f9d207a74cfac78029ae8ff5e08c"
tool_flags = {"CFLAGS": ["-fPIC"], "CXXFLAGS": ["-fPIC"]}
# FIXME int
hardening = ["!int"]


def init_configure(self):
    if not self.profile().cross:
        return

    # we build special host icu for cross
    self.configure_args.append(
        "--with-cross-build=" + str(self.chroot_cwd / "icu-host")
    )


def pre_configure(self):
    if not self.profile().cross:
        return

    # host build; first clean up potential old stuff
    self.rm("build-host", recursive=True, force=True)
    self.rm("icu-host", recursive=True, force=True)
    self.mkdir("build-host")
    # override most build-related environment
    self.do(
        self.chroot_cwd / "configure",
        "--prefix=/",
        "--sbindir=/bin",
        wrksrc="build-host",
        env={
            "CC": "cc",
            "LD": "ld",
            "CXX": "c++",
            "AR": "ar",
            "AS": "cc",
            "RANLIB": "ranlib",
            "STRIP": "strip",
            "CFLAGS": "-Os",
            "CXXFLAGS": "-Os",
            "LDFLAGS": "",
        },
    )
    self.make.build(wrksrc="build-host")
    self.mkdir("icu-host/config", parents=True)
    # copy over icucross
    for f in (self.cwd / "build-host/config").glob("icucross.*"):
        self.cp(f, "icu-host/config")
    # finally install host icu into special prefix
    self.make.install(
        ["DESTDIR=" + str(self.chroot_cwd / "icu-host")],
        wrksrc="build-host",
        default_args=False,
    )


def post_install(self):
    # FIXME: check if cross-endian icudt is still busted later
    self.install_license(self.builddir / self.wrksrc / "LICENSE")


@subpackage("icu-libs")
def _libs(self):
    return self.default_libs(extra=[f"usr/share/icu/{pkgver}/icudt*.dat"])


@subpackage("icu-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/icu", "usr/lib/icu"])
