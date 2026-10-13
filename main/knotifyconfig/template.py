pkgname = "knotifyconfig"
pkgver = "6.31.0"
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
sha256 = "185b326c746ee983c9dc19ff19cd40205f9be9dcd2b41e6619015f85abcc47e6"
hardening = ["vis"]


@subpackage("knotifyconfig-devel")
def _(self):
    return self.default_devel()
