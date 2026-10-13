pkgname = "purpose"
pkgver = "6.31.0"
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
url = "https://community.kde.org/Frameworks/index.html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/purpose-{pkgver}.tar.xz"
sha256 = "665b579a6b4c4d6f9f19a83fe802da70a65d38d9b23193471b5b64e65b7a55c3"
hardening = ["vis"]


@subpackage("purpose-devel")
def _(self):
    return self.default_devel()
