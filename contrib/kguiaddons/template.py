pkgname = "kguiaddons"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "plasma-wayland-protocols",
    "qt6-qtbase-devel",
    "qt6-qtwayland-devel",
]
pkgdesc = "KDE addons to QtGui"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/frameworks/kguiaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kguiaddons-{pkgver}.tar.xz"
sha256 = "e1519b1fc01ec3731c2926b69aee7a32c13e0f92178834fef484ac37d5dc3201"
hardening = ["vis", "!cfi"]


@subpackage("kguiaddons-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
