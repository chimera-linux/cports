pkgname = "kdegraphics-mobipocket"
pkgver = "24.05.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kio-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE plugins for mobipocket files"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/graphics/kdegraphics-mobipocket"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdegraphics-mobipocket-{pkgver}.tar.xz"
sha256 = "e45d8900c67aee3af0fb9b7f4ca646b7df9aeb2ac47f14be597eba01f9a124ad"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("kdegraphics-mobipocket-devel")
def _devel(self):
    return self.default_devel()
