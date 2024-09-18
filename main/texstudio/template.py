pkgname = "texstudio"
pkgver = "4.8.2"
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
sha256 = "363a289099911b41caac42d4fa6374794473ff6ed4487c2e4a07a7f59f866a45"
