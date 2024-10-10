pkgname = "kpkpass"
pkgver = "24.08.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kpkpass/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpkpass-{pkgver}.tar.xz"
sha256 = "3f095aab0b4f7b03fa84a4a59caab451b545e9a3ecc22dc4fee8edb59700cbbb"


@subpackage("kpkpass-devel")
def _(self):
    self.depends += ["karchive-devel"]
    return self.default_devel()
