pkgname = "frameworkintegration"
pkgver = "6.10.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/frameworkintegration-{pkgver}.tar.xz"
sha256 = "61fc35cffb0863517fa2072b96476bf109499d58fb3264062b40be528dd3af82"
hardening = ["vis"]


@subpackage("frameworkintegration-devel")
def _(self):
    self.depends += [
        "kcolorscheme-devel",
        "kiconthemes-devel",
        "kwidgetsaddons-devel",
    ]
    return self.default_devel()
