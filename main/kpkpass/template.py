pkgname = "kpkpass"
pkgver = "25.04.1"
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
sha256 = "a19900025670876e5586d99af6b7cc9fc19d31a75d63e41eb62def48c1a31e84"


@subpackage("kpkpass-devel")
def _(self):
    self.depends += ["karchive-devel"]
    return self.default_devel()
