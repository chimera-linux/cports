pkgname = "kdav"
pkgver = "6.9.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kdav/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdav-{pkgver}.tar.xz"
)
sha256 = "5ac5818e89bc9e8119f10a46bc3c8e54878db4e9a12c3a07481debc8d536cbd3"


@subpackage("kdav-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
