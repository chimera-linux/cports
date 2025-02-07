pkgname = "kcolorchooser"
pkgver = "24.12.2"
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
sha256 = "d0bfec7f4f8a4172ae3348307bd720380e5bf7550497f50a6fa94539ca55d4e8"


def post_install(self):
    self.install_license("COPYING")
