pkgname = "kde1-kdegames"
pkgver = "1.1.2"
pkgrel = 0
_gitrev = "b2b0d3aefc92ed9150babfad7e30a0c0054dc250"
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
pkgdesc = "KDE1 games"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/kde1-kdegames"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "766fe0a439c62f20193ec5dd4b609a72e2beee505f5bfa5739cccc9f5aada28b"
hardening = ["!int", "!format"]
options = ["!lto"]

tool_flags = {
    "CXXFLAGS": [
        "-Wno-format-security",
        "-Wno-writable-strings",
        "-Wno-c++11-narrowing",
        "-Wno-c++11-compat-deprecated-writable-strings",
    ],
}
