pkgname = "kunitconversion"
pkgver = "6.6.0"
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
sha256 = "a874f093a3e64f08d1d37e1142e17d78a112b613ece5cfa1f747dd1d26789f91"
hardening = ["vis"]


@subpackage("kunitconversion-devel")
def _(self):
    return self.default_devel()
