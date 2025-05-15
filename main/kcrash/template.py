pkgname = "kcrash"
pkgver = "6.14.0"
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
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcrash/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcrash-{pkgver}.tar.xz"
sha256 = "69d736be73bbe4a936f8996c3591a53c16816d4396d242d2e63dce079a268c34"
hardening = ["vis"]
# fails starting with 6.6
options = ["!check"]


@subpackage("kcrash-devel")
def _(self):
    return self.default_devel()
