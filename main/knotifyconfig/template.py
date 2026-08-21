pkgname = "knotifyconfig"
pkgver = "6.29.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/knotifyconfig-{pkgver}.tar.xz"
sha256 = "f0e75a0fa498fb0eccd5540257177e47da212095eb0b5ed4fc66935d42375b4e"
hardening = ["vis"]


@subpackage("knotifyconfig-devel")
def _(self):
    return self.default_devel()
