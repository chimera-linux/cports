pkgname = "kmime"
pkgver = "26.04.3"
pkgrel = 0
build_style = "cmake"
# fails on ppc64le with wrong encoding
make_check_args = ["-E", "(headertest|messagetest)"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "qt6-qttools-devel",
]
makedepends = [
    "kcodecs-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE library for mail messages"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kmime/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmime-{pkgver}.tar.xz"
sha256 = "a118b0d3b3ad2ebb35f73c675cffff575cd1b36ff5875d4f9fd4bce884bbae8a"


@subpackage("kmime-devel")
def _(self):
    self.depends += [
        "kcodecs-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
