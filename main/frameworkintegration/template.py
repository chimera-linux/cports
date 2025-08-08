pkgname = "frameworkintegration"
pkgver = "6.17.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
url = "https://api.kde.org/frameworks/frameworkintegration/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/frameworkintegration-{pkgver}.tar.xz"
sha256 = "9d9e011fac9d9967d94c43ed2a213d851263805e1db5dad08d812fe3f0e6ad12"
hardening = ["vis"]


@subpackage("frameworkintegration-devel")
def _(self):
    self.depends += [
        "kcolorscheme-devel",
        "kiconthemes-devel",
        "kwidgetsaddons-devel",
    ]
    return self.default_devel()
