pkgname = "kplotting"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE plotting library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kplotting/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kplotting-{pkgver}.tar.xz"
sha256 = "5e1883d107de16ccd7a27323c5575bb1ec2fec22c44c9c3199b3de885f5c18f4"


@subpackage("kplotting-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
