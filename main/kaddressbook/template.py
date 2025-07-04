pkgname = "kaddressbook"
pkgver = "25.04.3"
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
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-search-devel",
    "grantleetheme-devel",
    "kcmutils-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kiconthemes-devel",
    "kldap-devel",
    "kontactinterface-devel",
    "kuserfeedback-devel",
    "libkdepim-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
]
depends = ["kdepim-runtime"]
pkgdesc = "KDE address book"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://apps.kde.org/kaddressbook"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kaddressbook-{pkgver}.tar.xz"
)
sha256 = "a1c2781db83d7e33780e1705ca9565de5dd791bd54831299f90e933376a47820"


@subpackage("kaddressbook-devel")
def _(self):
    return self.default_devel()
