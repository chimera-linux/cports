pkgname = "openboard"
pkgver = "1.7.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_CXX_STANDARD=20"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "openssl3-devel",
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
license = "GPL-3.0-or-later"
url = "https://openboard.ch"
source = f"https://github.com/OpenBoard-org/OpenBoard/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9948a2fec3920679087422d5c1c1b18839e2a95cee5b485d7584bb972b54a13c"
