pkgname = "kmbox"
pkgver = "26.08.1"
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
url = "https://community.kde.org/KDE_PIM"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmbox-{pkgver}.tar.xz"
sha256 = "4bda0a789e010d383db7a56294941853cc2d878ddd57b33f1e08daeb2714a75b"


@subpackage("kmbox-devel")
def _(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()
