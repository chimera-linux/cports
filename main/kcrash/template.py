pkgname = "kcrash"
pkgver = "6.20.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kcoreaddons-devel", "qt6-qttools-devel"]
pkgdesc = "KDE Graceful handling of application crashes"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcrash/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcrash-{pkgver}.tar.xz"
sha256 = "1f42e9c54ead9f2d81b3ec5eacf55ab6ff4dd1c3a0721c68f3ab39ed46f35973"
hardening = ["vis"]
# fails starting with 6.6
options = ["!check"]


@subpackage("kcrash-devel")
def _(self):
    return self.default_devel()
