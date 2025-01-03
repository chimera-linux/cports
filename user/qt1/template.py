pkgname = "qt1"
pkgver = "1.45"
pkgrel = 0
_gitrev = "25d30943816da9c28cded9ac7ce23b94c2ff2a5c"
build_style = "cmake"
configure_args = [
    "-DBUILD_QT1_TUTORIAL=OFF",
    "-DBUILD_QT1_EXAMPLES=OFF",
    "-DINSTALL_QT_DOCS=OFF",
    "-DSYSTEM_ZLIB=ON",
]
hostmakedepends = [
    "byacc",
    "cmake",
    "flex",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glu-devel",
    "libx11-devel",
    "libxext-devel",
    "libxmu-devel",
    "mesa-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Qt 1.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:qt1"
url = "https://github.com/KDE/qt1"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "ca825b69643c95ecab771687ccd4a467e002bca6e651959b1afc2199f5f635a4"
hardening = ["!int", "!format"]
options = ["!lto"]

if self.profile().wordsize == 32:
    broken = "wraps time64-unsafe apis, breaking redirects"

tool_flags = {
    "CXXFLAGS": [
        "-std=gnu++98",
        "-Wno-c++11-compat-deprecated-writable-strings",
    ]
}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("qt1-devel")
def _(self):
    return self.default_devel()
