pkgname = "plasma-vault"
pkgver = "6.0.5"
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
pkgdesc = "KDE encrypted storage applet"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "(GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only AND LGPL-3.0-only)"
url = "https://invent.kde.org/plasma/plasma-vault"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-vault-{pkgver}.tar.xz"
sha256 = "2fe3cc73f7bef4d4c6476ea0cfd32e325d5b871fdfcff5c1141f203dde0be94d"


@subpackage("plasma-vault-gocryptfs")
def _gocryptfs(self):
    self.pkgdesc = f"{pkgdesc} (gocryptfs support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends += ["gocryptfs"]
    self.options = ["empty"]
    return []
