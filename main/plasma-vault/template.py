pkgname = "plasma-vault"
pkgver = "6.4.4"
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
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kservice-devel",
    "kwidgetsaddons-devel",
    "libksysguard-devel",
    "libplasma-devel",
    "networkmanager-qt-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["virtual:plasma-vault-backend!plasma-vault-none"]
pkgdesc = "KDE encrypted storage applet"
license = "(GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only AND LGPL-3.0-only)"
url = "https://invent.kde.org/plasma/plasma-vault"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-vault-{pkgver}.tar.xz"
sha256 = "2d843b1e37cb41b099c74142ad0d746942fdb447186d3e372ca6b7a3b051bc81"


@subpackage("plasma-vault-none")
def _(self):
    self.subdesc = "no backend"
    self.provides = ["plasma-vault-backend=0"]
    self.options = ["empty"]

    return []
