pkgname = "purpose"
pkgver = "6.9.0"
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
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE purpose-specific integrations"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://api.kde.org/frameworks/purpose/html/index.html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/purpose-{pkgver}.tar.xz"
sha256 = "1709a31d446e7be432179b7fcd2ee26e8e3b9fde0a39ab3557835643873ae558"
hardening = ["vis"]


@subpackage("purpose-devel")
def _(self):
    return self.default_devel()
