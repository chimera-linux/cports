pkgname = "kcolorchooser"
pkgver = "24.12.0"
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
sha256 = "afe552ddf0a4c76a4b81251649eeda1662b2a16dc8eba88c0be0ec4004b4674e"


def post_install(self):
    self.install_license("COPYING")
