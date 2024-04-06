pkgname = "kde1-kdeutils"
pkgver = "1.1.2"
pkgrel = 0
_gitrev = "0754b27dbe5e7470b24be83b539ff1c3d5092a48"
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
depends = [f"kde1-kdebase~{pkgver}"]
pkgdesc = "KDE1 utility applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/kde1-kdeutils"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "a93ae34b6eee502ec131ee0cba4ba222b200bfd2a3e20ebc1b12a646dd7d7fb0"
hardening = ["!int", "!format"]
options = ["!lto"]

tool_flags = {
    "CXXFLAGS": [
        "-std=gnu++98",
        "-Wno-c++11-extensions",
        "-Wno-c++11-compat-deprecated-writable-strings",
        "-Wno-implicit-const-int-float-conversion",
    ],
}
