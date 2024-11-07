pkgname = "kaddressbook"
pkgver = "24.08.3"
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
sha256 = "a94a91bab82e7fa1158965ea711c778b6370e88bb8cafe72d5f840932e13e4d7"


@subpackage("kaddressbook-devel")
def _(self):
    return self.default_devel()
