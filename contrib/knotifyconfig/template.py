pkgname = "knotifyconfig"
pkgver = "6.3.0"
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
sha256 = "ebf26f5e51e53eadb12e9a858aae9d55085d233c1f543879076452ac2900525d"
hardening = ["vis", "!cfi"]


@subpackage("knotifyconfig-devel")
def _devel(self):
    return self.default_devel()
