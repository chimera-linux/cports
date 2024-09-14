pkgname = "kcolorchooser"
pkgver = "24.08.1"
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
sha256 = "d8462f12d54e700aa6ec435cb8aef39fc42dad4842ee6e84fb6efebbe427703c"


def post_install(self):
    self.install_license("COPYING")
