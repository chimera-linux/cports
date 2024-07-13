pkgname = "kunitconversion"
pkgver = "6.4.0"
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
sha256 = "30e969467cb6f20c97e263e5381371ead458517758128022141d52272a660474"
hardening = ["vis", "!cfi"]


@subpackage("kunitconversion-devel")
def _devel(self):
    return self.default_devel()
