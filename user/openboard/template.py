pkgname = "openboard"
pkgver = "1.7.3"
pkgrel = 1
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
maintainer = "breakgimme <adam@plock.com>"
license = "GPL-3.0-or-later"
url = "https://openboard.ch"
source = f"https://github.com/OpenBoard-org/OpenBoard/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "55532df042e3a5b36e1f6f1e29916d3bbd01796d920782fa1f8a03438dcddd9c"
