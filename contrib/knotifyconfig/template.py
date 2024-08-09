pkgname = "knotifyconfig"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
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
]
pkgdesc = "KDE Configuration dialog for desktop notifications"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only"
url = "https://api.kde.org/frameworks/knotifyconfig/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/knotifyconfig-{pkgver}.tar.xz"
sha256 = "fb2ad6bffb54e6a05fab4dc871897beaba03a46d42fa290b56ee1fcbb2ee0594"
hardening = ["vis"]


@subpackage("knotifyconfig-devel")
def _devel(self):
    return self.default_devel()
