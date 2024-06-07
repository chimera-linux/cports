pkgname = "kcrash"
pkgver = "6.3.0"
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
sha256 = "65c67a0fe9b8da27d0efe8a44e16a348e7f602b29511062f263b555ebea48f41"
# FIXME: at least "./test_crasher ES" is broken
hardening = ["vis", "!cfi"]


@subpackage("kcrash-devel")
def _devel(self):
    return self.default_devel()
