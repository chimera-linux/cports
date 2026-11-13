pkgname = "syndication"
pkgver = "6.32.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kcodecs-devel", "qt6-qttools-devel"]
pkgdesc = "KDE's RSS/Atom parser library"
license = "LGPL-2.0-or-later AND BSD-2-Clause"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syndication-{pkgver}.tar.xz"
sha256 = "a1fc7e412e56ed9e457edd8c7295865007f89ea082c829245667f5321babfdf0"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("syndication-devel")
def _(self):
    return self.default_devel()
