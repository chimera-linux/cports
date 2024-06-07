pkgname = "kunitconversion"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
# most tests require network access, pass in cbuild chroot
make_check_args = ["-E", "(category|converter|currencytableinit)test"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Converting physical units"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kunitconversion/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kunitconversion-{pkgver}.tar.xz"
sha256 = "7db3f42dd0ff3df4eb748ee62883e8f23203ca32d143d3fa09deb0651095079b"
hardening = ["vis", "!cfi"]


@subpackage("kunitconversion-devel")
def _devel(self):
    return self.default_devel()
