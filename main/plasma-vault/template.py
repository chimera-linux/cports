pkgname = "plasma-vault"
pkgver = "6.2.1"
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
sha256 = "79762528465cbd8e3af0fb75fda184dc6dd5d09df60b48701027fa2ceec9688f"


@subpackage("plasma-vault-gocryptfs")
def _(self):
    self.subdesc = "gocryptfs support"
    self.install_if = [self.parent]
    self.depends += ["gocryptfs"]
    self.options = ["empty"]
    return []
