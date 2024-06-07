pkgname = "breeze-icons"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBINARY_ICONS_RESOURCE=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "python-lxml",
]
makedepends = [
    "qt6-qtbase-devel",
]
checkdepends = [
    "fdupes",
]
pkgdesc = "Breeze icon themes"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-or-later"
url = "https://api.kde.org/frameworks/breeze-icons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/breeze-icons-{pkgver}.tar.xz"
sha256 = "67266378f2d7dbf13dc4f691de43f30b5aca4e4a3336e9f60f0efba2a474e626"
broken_symlinks = [
    # broken symbolic links to 24
    "usr/share/icons/breeze*/animations/24@*x",  # breeze{,-dark}/animations/24@{2,3}x
    "usr/share/icons/breeze/emotes/24@*x",  # 24@{2,3}x
    # broken symbolic link to fingerprint.svg
    "usr/share/icons/breeze/actions/24/fingerprint-symbolic.svg",
]
hardening = ["vis", "!cfi"]


@subpackage("breeze-icons-devel")
def _devel(self):
    return self.default_devel()
