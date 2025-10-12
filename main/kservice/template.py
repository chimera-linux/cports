pkgname = "kservice"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
# flaky tests when parallel
make_check_args = ["-j1", "-E", "(kservicetest|kapplicationtradertest)"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Plugin framework for desktop services"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kservice/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kservice-{pkgver}.tar.xz"
sha256 = "815e08493e6bb90f82e92726aff78bdcf1358a942972fc75112e99cb840961bd"
hardening = ["vis"]


@subpackage("kservice-devel")
def _(self):
    self.depends += ["kconfig-devel", "kcoreaddons-devel"]

    return self.default_devel()
