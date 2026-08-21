pkgname = "frameworkintegration"
pkgver = "6.29.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
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
    "qt6-qttools-devel",
    # TODO: packagekitqt6 + AppStreamQt 1.0? (KPackage install handler binaries)
]
pkgdesc = "Integration of Qt application with KDE workspaces"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/frameworkintegration-{pkgver}.tar.xz"
sha256 = "be01225efe9063e4c4a23dae47ebafed437f1cd06d73ab2de77dfb99e35785b8"
hardening = ["vis"]


@subpackage("frameworkintegration-devel")
def _(self):
    self.depends += [
        "kcolorscheme-devel",
        "kiconthemes-devel",
        "kwidgetsaddons-devel",
    ]
    return self.default_devel()
