pkgname = "purpose"
pkgver = "6.3.0"
pkgrel = 0
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
sha256 = "bf296f6646bdcfef4aebba4d04ec03e7e72a545552b9b765a8fbfc625ee6ec17"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("purpose-devel")
def _devel(self):
    return self.default_devel()
