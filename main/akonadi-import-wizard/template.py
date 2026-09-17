pkgname = "akonadi-import-wizard"
pkgver = "26.08.1"
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
    "akonadi-devel",
    "karchive-devel",
    "kauth-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kmailtransport-devel",
    "mailcommon-devel",
    "mailimporter-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE Akonadi assistant for importing data into KDEPIM"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://invent.kde.org/pim/akonadi-import-wizard"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-import-wizard-{pkgver}.tar.xz"
sha256 = "af5c26b74dce64974403bac9182c8477fbfd99369978670b5e2aee588fad4699"


@subpackage("akonadi-import-wizard-devel")
def _(self):
    self.depends += ["kmailtransport-devel"]
    return self.default_devel()
