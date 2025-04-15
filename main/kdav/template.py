pkgname = "kdav"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
# hangs forever
make_check_args = ["-E", "davitemfetchjob"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE DAV library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kdav/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdav-{pkgver}.tar.xz"
)
sha256 = "d767e8f5158d7f4c1f588f17286177145880d80cfb2e215f554a6c820f86b0d9"


@subpackage("kdav-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
