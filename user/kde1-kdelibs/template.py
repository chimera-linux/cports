pkgname = "kde1-kdelibs"
pkgver = "1.1.2"
pkgrel = 0
_gitrev = "eec7a2b34bf3aa14f775be132a9ff9c7767c5f62"
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
    "libxext-devel",
    "libx11-devel",
    "qt1-devel",
]
pkgdesc = "KDE1 libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.0-only"
url = "https://github.com/KDE/kde1-kdelibs"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "e84b87c53d62dd0008c6dba22468e25c0fb15ffa7cdf4f5ef6d6a369985f4d4e"
hardening = ["!int", "!format"]
options = ["!lto"]

tool_flags = {
    "CXXFLAGS": [
        "-std=gnu++98",
    ]
}


@subpackage("kde1-kdelibs-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
