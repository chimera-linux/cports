pkgname = "frameworkintegration"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcolorscheme-devel",
    "kconfig-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kpackage-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    # TODO: packagekitqt6 + AppStreamQt 1.0? (KPackage install handler binaries)
]
pkgdesc = "Integration of Qt application with KDE workspaces"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/frameworkintegration/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/frameworkintegration-{pkgver}.tar.xz"
sha256 = "94700551b3373f792b27ea6ca3013c7bda8f6b63260b918b3c1eec0d83ad4c7f"
hardening = ["vis", "!cfi"]


@subpackage("frameworkintegration-devel")
def _devel(self):
    self.depends += [
        "kcolorscheme-devel",
        "kiconthemes-devel",
        "kwidgetsaddons-devel",
    ]
    return self.default_devel()
