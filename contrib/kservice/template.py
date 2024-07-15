pkgname = "kservice"
pkgver = "6.4.0"
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
sha256 = "cdb9d7e3c6ffa3f7da8ff33a7b3ecb95ef8451bdefb97bcb79452fa03e7d8a1f"
hardening = ["vis"]


@subpackage("kservice-devel")
def _devel(self):
    self.depends += ["kconfig-devel", "kcoreaddons-devel"]

    return self.default_devel()
