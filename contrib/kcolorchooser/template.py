pkgname = "kcolorchooser"
pkgver = "24.05.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://apps.kde.org/kcolorchooser"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kcolorchooser-{pkgver}.tar.xz"
)
sha256 = "2148ea2b035c864bb68ca66fde17696e998fbc89f5e010f4c5c54d94dc14d7e1"


def post_install(self):
    self.install_license("COPYING")
