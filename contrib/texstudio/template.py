pkgname = "texstudio"
pkgver = "4.8.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "hunspell-devel",
    "libpoppler-devel",
    "poppler-qt-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "quazip-devel",
]
pkgdesc = "Integrated writing environment for creating LaTeX documents"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://www.texstudio.org"
source = f"https://github.com/texstudio-org/texstudio/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "351a8111506bfb9cd79a6284f7b92d7c5a1da5ac22c25f6788040ce3b9b1080a"
