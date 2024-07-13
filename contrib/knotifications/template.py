pkgname = "knotifications"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "libcanberra-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Desktop notifications"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/knotifications/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/knotifications-{pkgver}.tar.xz"
sha256 = "77e9b680066dc49c8d5e23ac6291fbba05328dda327d5c34ca3141e1ffeb25dc"
# CFI: kills systemsettings (going from "Spell Check" to "Region & Language" and attempting close) in ~NotifyByAudio()
# https://invent.kde.org/frameworks/knotifications/-/blob/v6.4.0/src/notifybyaudio.cpp#L56
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("knotifications-devel")
def _devel(self):
    return self.default_devel()
