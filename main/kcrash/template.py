pkgname = "kcrash"
pkgver = "6.18.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kcoreaddons-devel", "qt6-qttools-devel"]
pkgdesc = "KDE Graceful handling of application crashes"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcrash/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcrash-{pkgver}.tar.xz"
sha256 = "a66293821b151f575fcfb59848578749e248c5baa2f262ac86725d0f64b324e0"
hardening = ["vis"]
# fails starting with 6.6
options = ["!check"]


@subpackage("kcrash-devel")
def _(self):
    return self.default_devel()
