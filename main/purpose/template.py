pkgname = "purpose"
pkgver = "6.27.0"
pkgrel = 0
build_style = "cmake"
# menutest: ??
# alternativesmodeltest: tries to reach remote url
make_check_args = ["-E", "(menutest|alternativesmodeltest)"]
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
    "kitemmodels-devel",
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
sha256 = "c4e348fa5ac990a77b3926105c62bc4f2dddaf8d7554c43ee4f18de3d16a3699"
hardening = ["vis"]


@subpackage("purpose-devel")
def _(self):
    return self.default_devel()
