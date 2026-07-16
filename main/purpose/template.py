pkgname = "purpose"
pkgver = "6.28.0"
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
sha256 = "c2be01e1aaf2ab14ba6f05582d7c4a29e144dd96258d86b208f58c34bfa83672"
hardening = ["vis"]


@subpackage("purpose-devel")
def _(self):
    return self.default_devel()
