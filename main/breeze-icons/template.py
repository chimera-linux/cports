pkgname = "breeze-icons"
pkgver = "6.17.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBINARY_ICONS_RESOURCE=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
    "python-lxml",
]
makedepends = ["qt6-qtbase-devel"]
checkdepends = ["fdupes"]
pkgdesc = "Breeze icon themes"
license = "LGPL-3.0-or-later"
url = "https://api.kde.org/frameworks/breeze-icons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/breeze-icons-{pkgver}.tar.xz"
sha256 = "4ffc75886e9a14a2a02da4871600b8c0b5a40756b8e99cbecfb515696d93c3b8"
broken_symlinks = [
    # broken symbolic links to 24
    "usr/share/icons/breeze*/animations/24@*x",  # breeze{,-dark}/animations/24@{2,3}x
    "usr/share/icons/breeze/emotes/24@*x",  # 24@{2,3}x
]
hardening = ["vis"]
# over 300 broken symbolic links for size 24 svgs since 6.15..
options = ["brokenlinks"]


@subpackage("breeze-icons-devel")
def _(self):
    return self.default_devel()
