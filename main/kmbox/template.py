pkgname = "kmbox"
pkgver = "24.12.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kmbox/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmbox-{pkgver}.tar.xz"
sha256 = "daca1148d770a69f95fae08650d066940f3a2d92347499fcbdc92706d9d8d9fc"


@subpackage("kmbox-devel")
def _(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()
