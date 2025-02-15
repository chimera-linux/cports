pkgname = "kcrash"
pkgver = "6.11.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcrash-{pkgver}.tar.xz"
sha256 = "ba13e9f5dd2b40125d5d61d29b612db6383315dc0f510cc1f0e33bb6c9b0ae89"
hardening = ["vis"]
# fails starting with 6.6
options = ["!check"]


@subpackage("kcrash-devel")
def _(self):
    return self.default_devel()
