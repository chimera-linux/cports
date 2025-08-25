pkgname = "kcrash"
pkgver = "6.17.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kcoreaddons-devel", "qt6-qttools-devel"]
pkgdesc = "KDE Graceful handling of application crashes"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcrash/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcrash-{pkgver}.tar.xz"
sha256 = "52f4bddc642e68e96f8f18b34bba803b8f9f93cb8cf5e1d1aabccfd3c5285e13"
hardening = ["vis"]
# fails starting with 6.6
options = ["!check"]


@subpackage("kcrash-devel")
def _(self):
    return self.default_devel()
