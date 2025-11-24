pkgname = "attica"
pkgver = "6.20.0"
pkgrel = 0
build_style = "cmake"
# requires network access and passes in cbuild chroot
make_check_args = ["-E", "providertest"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = ["qt6-qttools-devel"]
pkgdesc = "Freedesktop Open Collaboration Services (OCS) binding for Qt"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/attica/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/attica-{pkgver}.tar.xz"
sha256 = "8ef95ad2798763202cdd659521bbe64ca58ec8ca68465eace4a817a2ff2e4dc4"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()
