pkgname = "openboard"
pkgver = "1.7.1"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DCMAKE_CXX_STANDARD=20"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "openssl-devel",
    "poppler-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebengine-devel",
    "quazip-devel",
]
pkgdesc = "Interactive whiteboard application"
maintainer = "breakgimme <adam@plock.com>"
license = "GPL-3.0-or-later"
url = "https://openboard.ch"
source = f"https://github.com/OpenBoard-org/OpenBoard/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5c9fcb54bc1598b4b7026e6ecca07137660dd3d45bda472a5710acf600a2a22f"


@subpackage("openboard-locale")
def _(self):
    self.install_if = [self.parent, "base-locale"]
    return ["usr/share/openboard/i18n"]
