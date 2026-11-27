pkgname = "lxqt-archiver"
pkgver = "1.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "pkgconf", "perl"]
makedepends = [
    "json-glib-devel",
    "libexif-devel",
    "libfm-qt-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Simple and lightweight Qt file archiver"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/lxqt-archiver"
source = f"{url}/releases/download/{pkgver}/lxqt-archiver-{pkgver}.tar.xz"
sha256 = "da09ac7e80cdf5ced408c500e1de58196798ff583eded5385ac9da11dae82c78"
