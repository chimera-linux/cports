pkgname = "kaddressbook"
pkgver = "24.05.2"
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
    "kontactinterface-devel",
    "kuserfeedback-devel",
    "libkdepim-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
]
depends = ["kdepim-runtime"]
pkgdesc = "KDE address book"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://apps.kde.org/kaddressbook"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kaddressbook-{pkgver}.tar.xz"
)
sha256 = "68494e62c91c2fdb9e3f436b395aa37f16723d4a695f8f04ce58b653c79bb8bc"


@subpackage("kaddressbook-devel")
def _devel(self):
    return self.default_devel()
