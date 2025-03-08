pkgname = "kpkpass"
pkgver = "24.12.3"
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
sha256 = "cf22c45a942f2723f309542bf0499896c27d381521caf0b2cc9465246a7d74a9"


@subpackage("kpkpass-devel")
def _(self):
    self.depends += ["karchive-devel"]
    return self.default_devel()
