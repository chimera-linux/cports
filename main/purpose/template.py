pkgname = "purpose"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
    "qt6-qttools-devel",
]
depends = ["accounts-qml-module"]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE purpose-specific integrations"
license = "LGPL-2.1-only"
url = "https://api.kde.org/frameworks/purpose/html/index.html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/purpose-{pkgver}.tar.xz"
sha256 = "799ff3e69872400d2fa6e5e2c91fed66ed6bd0d7a9163efc004eee0bf6d093a2"
hardening = ["vis"]


@subpackage("purpose-devel")
def _(self):
    return self.default_devel()
