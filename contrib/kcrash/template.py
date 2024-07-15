pkgname = "kcrash"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kcoreaddons-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Graceful handling of application crashes"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcrash/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcrash-{pkgver}.tar.xz"
sha256 = "011215bc952a430c1d093b0bf5cdad7057c9a9098d86116e69c6dd1000567697"
hardening = ["vis"]


@subpackage("kcrash-devel")
def _devel(self):
    return self.default_devel()
