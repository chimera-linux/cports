pkgname = "kde1-kdetoys"
pkgver = "1.1.2"
pkgrel = 0
_gitrev = "66a0fb39185d9733d294156881ba631de53e432d"
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
pkgdesc = "KDE1 toys"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/kde1-kdetoys"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "1ed02bca7a0eb825a62feb9099124939436969f2a839a056cef02e53503e7c6a"
hardening = ["!int", "!format"]
options = ["!lto"]

tool_flags = {
    "CFLAGS": [
        "-Wno-deprecated-non-prototype",
    ],
    "CXXFLAGS": [
        "-std=gnu++98",
        "-Wno-c++11-compat-deprecated-writable-strings",
    ],
}
