pkgname = "kde1-kdenetwork"
pkgver = "1.1.2"
pkgrel = 0
_gitrev = "f48d8610aca90f394631568b7bbe464d74b0011d"
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kde1-kdelibs-devel",
]
pkgdesc = "KDE1 network applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/kde1-kdenetwork"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "a3d17fc7b3c6b6808f3128239ea894790747295e868836334588e42a659318f4"
hardening = ["!int", "!format"]
options = ["!lto"]

tool_flags = {
    "CXXFLAGS": [
        "-std=gnu++98",
        "-Wno-c++11-compat-deprecated-writable-strings",
    ],
}
