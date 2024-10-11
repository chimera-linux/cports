pkgname = "attica"
pkgver = "6.7.0"
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
sha256 = "daa5c07b474899e16b42710e03d0590936bce0f54800239d633d48caa3be0d7d"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()
