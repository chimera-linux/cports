pkgname = "libkgapi"
pkgver = "25.12.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcalendarcore-devel",
    "kcontacts-devel",
    "kwallet-devel",
    "libsasl-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE library for accessing Google services"
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/libkgapi/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkgapi-{pkgver}.tar.xz"
sha256 = "42086c3f5cec31be3c379b43ae80e32beb29055159d1670e00ad7f0892632c1c"
# tests all segfault with missing data
options = ["!check"]


@subpackage("libkgapi-devel")
def _(self):
    self.depends += [
        "kcontacts-devel",
        "kcalendarcore-devel",
    ]
    return self.default_devel()
