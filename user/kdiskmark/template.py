pkgname = "kdiskmark"
pkgver = "3.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = ["polkit-qt-1-devel", "qt6-qtbase-devel", "qt6-qttools-devel"]
depends = ["fio"]
pkgdesc = "Disk benchmark tool"
license = "GPL-3.0-only"
url = "https://github.com/JonMagon/KDiskMark"
source = f"{url}/releases/download/{pkgver}/kdiskmark-{pkgver}-source.tar.gz"
sha256 = "c42f302d707fc9f730b5ef2f8866132e967b9263358539a9429b1dbad7c646ef"
hardening = ["vis"]
