pkgname = "kcodecs"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gperf",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Collection of methods to manipulate strings using various encodings"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcodecs/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcodecs-{pkgver}.tar.xz"
sha256 = "d040fb03510ca90942e54323b1afd26ec00d459b1b2c54e6eeeece5166842f2f"
# FIXME: at least a few tests fail
hardening = ["vis", "!cfi"]


@subpackage("kcodecs-devel")
def _devel(self):
    return self.default_devel()
