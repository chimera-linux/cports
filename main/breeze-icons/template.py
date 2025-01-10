pkgname = "breeze-icons"
pkgver = "6.10.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/breeze-icons-{pkgver}.tar.xz"
sha256 = "fe458eb957be655ea801d41f1dd3c4cfa829e7ba6040b38d69d09f6b69c31e2a"
broken_symlinks = [
    # broken symbolic links to 24
    "usr/share/icons/breeze*/animations/24@*x",  # breeze{,-dark}/animations/24@{2,3}x
    "usr/share/icons/breeze/emotes/24@*x",  # 24@{2,3}x
    # broken symbolic link to fingerprint.svg
    "usr/share/icons/breeze/actions/24/fingerprint-symbolic.svg",
]
hardening = ["vis"]


@subpackage("breeze-icons-devel")
def _(self):
    return self.default_devel()
