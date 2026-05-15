pkgname = "kdiskmark"
pkgver = "3.2.0"
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
sha256 = "6f03206d0b57383fd9d37a49c45d4d644ccb3e4dd53c81dda9250787a4e9d57d"
hardening = ["vis"]
