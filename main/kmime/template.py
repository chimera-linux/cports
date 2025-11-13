pkgname = "kmime"
pkgver = "25.08.3"
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
sha256 = "1f4fca3bff999fd84d9cf3d8073df7d3c1693ad8554b5600174e4a9aa1837f01"


@subpackage("kmime-devel")
def _(self):
    self.depends += [
        "kcodecs-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
