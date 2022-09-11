pkgname = "flac"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-rpath", "--disable-doxygen-docs", "--disable-xmms-plugin",
    f"--with-ogg={self.profile().sysroot / 'usr'}", "--disable-thorough-tests"
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "nasm", "gmake"]
makedepends = ["libogg-devel"]
pkgdesc = "Free Lossless Audio Codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "http://flac.sourceforge.net"
source = f"https://downloads.xiph.org/releases/flac/{pkgname}-{pkgver}.tar.xz"
sha256 = "af41c0733c93c237c3e52f64dd87e3b0d9af38259f1c7d11e8cbf583c48c2506"

match self.profile().arch:
    case "ppc64le":
        configure_args += ["--enable-altivec", "--enable-vsx"]
    case "ppc64":
        configure_args += ["--enable-altivec", "--disable-vsx"]

def post_install(self):
    self.install_license("COPYING.Xiph")

@subpackage("libflac")
def _lib(self):
    self.pkgdesc = f"{pkgname} (runtime library)"
    return self.default_libs()

@subpackage("flac-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/share/doc"
    ])
