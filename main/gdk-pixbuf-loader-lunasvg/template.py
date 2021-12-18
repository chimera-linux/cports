pkgname = "gdk-pixbuf-loader-lunasvg"
_commit = "f6e9ad25d0a258da3f0cae11a60babf72daf8ea3"
_lunasvg_ver = "2.3.0"
pkgver = "0.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "cmake", "pkgconf"]
makedepends = ["libglib-devel", "gdk-pixbuf-devel"]
provides = ["gdk-pixbuf-loader-svg=0"]
pkgdesc = "Alternative SVG loader for gdk-pixbuf"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/q66/gdk-pixbuf-loader-lunasvg"
source = [
    f"{url}/archive/{_commit}.tar.gz",
    f"https://github.com/sammycage/lunasvg/archive/refs/tags/v{_lunasvg_ver}.tar.gz",
]
sha256 = [
    "c601f2cff4b961646635ed9bf627f0661d61b453ae6229aecc141729a4d4fc86",
    "c1a4faef9bc2f65f8c64a2770c7e10753178e7318b8f6e09b1a4f1a495524e7c",
]

def post_extract(self):
    for f in (self.cwd / f"{pkgname}-{_commit}").glob("*"):
        self.mv(f, ".")
    self.mv(f"lunasvg-{_lunasvg_ver}", "subprojects/lunasvg")

def post_install(self):
    self.install_license("COPYING")
    self.install_license("subprojects/lunasvg/LICENSE")
    self.rm(self.destdir / "usr/lib/liblunasvg.a")
