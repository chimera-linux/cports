pkgname = "attica"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
# requires network access and passes in cbuild chroot
make_check_args = ["-E", "providertest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
]
pkgdesc = "Freedesktop Open Collaboration Services (OCS) binding for Qt"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/attica/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/attica-{pkgver}.tar.xz"
sha256 = "acccb7ff62e1e421faa5ffd381b41777d0c7bfba268fae1ed802b51a6bd98a87"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()
