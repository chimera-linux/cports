pkgname = "kmbox"
pkgver = "25.08.3"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kmime-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM mbox access library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kmbox/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmbox-{pkgver}.tar.xz"
sha256 = "316185fa387e38561bdd2e0a0b984a3fc00832a62271d06dcfebce1dc7f0558c"


@subpackage("kmbox-devel")
def _(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()
