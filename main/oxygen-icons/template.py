pkgname = "oxygen-icons"
pkgver = "6.32.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
]
checkdepends = [
    "fdupes",
]
pkgdesc = "Oxygen icon themes"
license = "GPL-2.0-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/oxygen-icons-{pkgver}.tar.xz"
sha256 = "743b5277c63592d84a51a643e5381d6afbc5c7563ff775faae6005311d1bfccd"


def post_extract(self):
    # wrong copies that break icon cache gen
    self.rm("simbolicActions/22x22/actions/go-first copy.svg")
    self.rm("simbolicActions/24x24/actions/go-first copy.svg")
    self.rm("simbolicActions/48x48/actions/go-first copy.svg")
