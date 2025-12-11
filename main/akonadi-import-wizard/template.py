pkgname = "akonadi-import-wizard"
pkgver = "25.12.0"
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
sha256 = "ee536787f8ca4f8299be72990b94cf24b61634e4c8318e3cf5b6a12ad513628b"


@subpackage("akonadi-import-wizard-devel")
def _(self):
    self.depends += ["kmailtransport-devel"]
    return self.default_devel()
