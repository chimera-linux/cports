pkgname = "texstudio"
pkgver = "4.8.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "hunspell-devel",
    "poppler-devel",
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
sha256 = "5dc43932272eccda23763b6d28c08df344ce2107ef2fd69734daaeb5a8ad1893"
