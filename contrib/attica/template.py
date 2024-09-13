pkgname = "attica"
pkgver = "6.6.0"
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
sha256 = "e2370e7f0a0e4721180c364342f47bc974cf3b45c45c7ce9e70c5d9ba5230be3"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()
