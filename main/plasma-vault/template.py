pkgname = "plasma-vault"
pkgver = "6.8.1"
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
sha256 = "0da7a15ce222d352b34f901c6331771a54be0d2ecf3c1a532a4373b212d26f74"


@subpackage("plasma-vault-none")
def _(self):
    self.subdesc = "no backend"
    self.provides = ["plasma-vault-backend=0"]
    self.options = ["empty"]

    return []
