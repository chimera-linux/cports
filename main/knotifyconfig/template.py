pkgname = "knotifyconfig"
pkgver = "6.7.0"
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
sha256 = "4227da7a18f9ba83b34bf54b6d3fc168dc0726bca149d2f89585bb54ab138295"
hardening = ["vis"]


@subpackage("knotifyconfig-devel")
def _(self):
    return self.default_devel()
