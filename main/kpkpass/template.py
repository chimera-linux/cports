pkgname = "kpkpass"
pkgver = "25.04.0"
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
sha256 = "39bde1831f700555c89ac06214510b9f1e58f2f5e5836ec11196b07ff1f6216a"


@subpackage("kpkpass-devel")
def _(self):
    self.depends += ["karchive-devel"]
    return self.default_devel()
