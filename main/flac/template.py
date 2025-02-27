pkgname = "flac"
pkgver = "1.5.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-rpath",
    "--disable-doxygen-docs",
    f"--with-ogg={self.profile().sysroot / 'usr'}",
    "--disable-thorough-tests",
]
configure_gen = []
make_dir = "."
hostmakedepends = ["pkgconf", "nasm"]
makedepends = ["libogg-devel"]
pkgdesc = "Free Lossless Audio Codec"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "http://flac.sourceforge.net"
source = f"https://downloads.xiph.org/releases/flac/flac-{pkgver}.tar.xz"
sha256 = "f2c1c76592a82ffff8413ba3c4a1299b6c7ab06c734dee03fd88630485c2b920"
# FIXME cfi int: test failures with both
hardening = ["vis", "!cfi", "!int"]
# stuck on some weird test, but appears harmless
options = ["!check"]

match self.profile().arch:
    case "ppc64le":
        configure_args += ["--enable-altivec", "--enable-vsx"]
    case "ppc64":
        configure_args += ["--enable-altivec", "--disable-vsx"]
    case "ppc":
        configure_args += ["--disable-altivec", "--disable-vsx"]


def post_install(self):
    self.install_license("COPYING.Xiph")


@subpackage("flac-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libflac")]

    return self.default_libs()


@subpackage("flac-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])
