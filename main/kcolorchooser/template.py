pkgname = "kcolorchooser"
pkgver = "25.08.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "kxmlgui-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE color palette tool"
license = "MIT"
url = "https://apps.kde.org/kcolorchooser"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kcolorchooser-{pkgver}.tar.xz"
)
sha256 = "6acece03b3804a610822d058fbbbcdabec3fe1ada6a8bffed6d369526930be67"


def post_install(self):
    self.install_license("COPYING")
