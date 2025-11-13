pkgname = "kpkpass"
pkgver = "25.08.3"
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
    "karchive-devel",
    "qt6-qtbase-devel",
    "shared-mime-info",
]
pkgdesc = "KDE PIM library for Apple Wallet pass files"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kpkpass/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpkpass-{pkgver}.tar.xz"
sha256 = "3802a6f23edd901be975c03b3eb63e478e9384386d883b2289fb598edf3e758b"


@subpackage("kpkpass-devel")
def _(self):
    self.depends += ["karchive-devel"]
    return self.default_devel()
