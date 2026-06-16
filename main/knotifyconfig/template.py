pkgname = "knotifyconfig"
pkgver = "6.27.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "ki18n-devel",
    "kio-devel",
    "knotifications-devel",
    "kxmlgui-devel",
    "libcanberra-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Configuration dialog for desktop notifications"
license = "LGPL-2.0-only"
url = "https://api.kde.org/frameworks/knotifyconfig/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/knotifyconfig-{pkgver}.tar.xz"
sha256 = "81861316d615e7e5ff07143c1d58d9b52cadc5e02ab38c8f2677c01f71e51f26"
hardening = ["vis"]


@subpackage("knotifyconfig-devel")
def _(self):
    return self.default_devel()
