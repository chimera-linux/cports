pkgname = "purpose"
pkgver = "6.2.0"
pkgrel = 2
build_style = "cmake"
# ??
make_check_args = ["-E", "(menutest)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kaccounts-integration-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdeclarative-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kservice-devel",
    "prison-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["accounts-qml-module"]
checkdepends = ["xwayland-run"] + depends
pkgdesc = "KDE purpose-specific integrations"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://api.kde.org/frameworks/purpose/html/index.html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/purpose-{pkgver}.tar.xz"
sha256 = "55b02d49387b76f54e3bec48f82cd78f398b5403bc8d10d482bfff7e30a0028a"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("purpose-devel")
def _devel(self):
    return self.default_devel()
