pkgname = "kaddressbook"
pkgver = "24.12.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://apps.kde.org/kaddressbook"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kaddressbook-{pkgver}.tar.xz"
)
sha256 = "82b5f35e68d41b586b4fc265945a489abd564784a662dc0fabaa9ad54b8ec537"


@subpackage("kaddressbook-devel")
def _(self):
    return self.default_devel()
