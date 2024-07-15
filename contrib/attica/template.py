pkgname = "attica"
pkgver = "6.4.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/attica/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/attica-{pkgver}.tar.xz"
sha256 = "c3f66e2c02ef313fa240f5aabfbcad3969fdfc788c9604d1cf7e4e0893fb5740"
hardening = ["vis"]


@subpackage("attica-devel")
def _devel(self):
    return self.default_devel()
