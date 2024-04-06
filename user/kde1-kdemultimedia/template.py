pkgname = "kde1-kdemultimedia"
pkgver = "1.1.2"
pkgrel = 0
_gitrev = "f38454787b319382a7298de4b85a5f9e7dda5ff6"
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kde1-kdelibs-devel",
    "linux-headers",
]
pkgdesc = "KDE1 multimedia applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/kde1-kdemultimedia"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "d0ce369e6dfcf10ec11c756b6850bc93bd96cb888ad86c864f357e0caf3d4c72"
hardening = ["!int", "!format"]
options = ["!lto"]

tool_flags = {
    "CXXFLAGS": [
        "-std=gnu++98",
        "-Wno-c++11-compat-deprecated-writable-strings",
    ],
}
