pkgname = "syndication"
pkgver = "6.29.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kcodecs-devel", "qt6-qttools-devel"]
pkgdesc = "KDE's RSS/Atom parser library"
license = "LGPL-2.0-or-later AND BSD-2-Clause"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syndication-{pkgver}.tar.xz"
sha256 = "f5a00d13eaf0401e9e4f3ffccda4876e2bcf84fb8dc2613a5d087971b377df1f"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("syndication-devel")
def _(self):
    return self.default_devel()
