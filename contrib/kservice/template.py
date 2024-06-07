pkgname = "kservice"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
# flaky tests when parallel
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Plugin framework for desktop services"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kservice/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kservice-{pkgver}.tar.xz"
sha256 = "a0564d62c1e0f2293b0dcb39cf814c2856111242b8621b33f52a70fda1a8fe54"
# FIXME: cfi breaks at least k{applicationtrader,mimeassociations}test
hardening = ["vis", "!cfi"]


@subpackage("kservice-devel")
def _devel(self):
    self.depends += ["kconfig-devel", "kcoreaddons-devel"]

    return self.default_devel()
