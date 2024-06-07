pkgname = "attica"
pkgver = "6.3.0"
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
sha256 = "abaf3a113a002d5d8435a3a75020f98c574290d2c552a5f256291d0418cc59ed"
# FIXME: cfi causes crash when pressing "Get New Plugins..." button in the
# "Wallpaper" section of Plasma's system settings app
hardening = ["vis", "!cfi"]


@subpackage("attica-devel")
def _devel(self):
    return self.default_devel()
