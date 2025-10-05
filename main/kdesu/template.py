pkgname = "kdesu"
pkgver = "6.18.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kpty-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Framework for running commands as root"
license = "GPL-2.0-only"
url = "https://api.kde.org/frameworks/kdesu/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdesu-{pkgver}.tar.xz"
sha256 = "3203b047113cf08bca3981ede657e45b417a7cd0f2879bb4f9e901ad4e594616"
hardening = ["vis"]


@subpackage("kdesu-devel")
def _(self):
    self.depends += ["kpty-devel"]
    return self.default_devel()
