pkgname = "kaddressbook"
pkgver = "25.08.3"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
sha256 = "8535f34ccd1428629072afd5e2e739c59e29e4a0c67e444f09917ca43017aa57"


@subpackage("kaddressbook-devel")
def _(self):
    return self.default_devel()
