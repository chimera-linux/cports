pkgname = "kde1-kdegraphics"
pkgver = "1.1.2"
pkgrel = 0
_gitrev = "4bf9d8a32634d7dcc9c6f08be2cd22a11b8f1fe6"
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "giflib-devel",
    "kde1-kdelibs-devel",
]
pkgdesc = "KDE1 graphics applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/kde1-kdegraphics"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "dffc55ea4552324a4fbb025c8ed5baea5fe80995ead0b60b4edb08f7e256bce7"
hardening = ["!int", "!format"]
options = ["!lto"]

tool_flags = {
    "CXXFLAGS": [
        "-std=gnu++98",
        "-Wno-c++11-compat-deprecated-writable-strings",
    ],
}
