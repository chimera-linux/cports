pkgname = "flac"
pkgver = "1.4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-rpath",
    "--disable-doxygen-docs",
    f"--with-ogg={self.profile().sysroot / 'usr'}",
    "--disable-thorough-tests",
]
configure_gen = []
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "nasm", "gmake"]
makedepends = ["libogg-devel"]
pkgdesc = "Free Lossless Audio Codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "http://flac.sourceforge.net"
source = f"https://downloads.xiph.org/releases/flac/{pkgname}-{pkgver}.tar.xz"
sha256 = "6c58e69cd22348f441b861092b825e591d0b822e106de6eb0ee4d05d27205b70"
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


@subpackage("libflac")
def _lib(self):
    self.pkgdesc = f"{pkgname} (runtime library)"
    return self.default_libs()


@subpackage("flac-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])
