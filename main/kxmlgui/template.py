pkgname = "kxmlgui"
pkgver = "6.18.0"
pkgrel = 0
build_style = "cmake"
# unpackaged pyside6
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kitemviews-devel",
    "qt6-qtbase-private-devel",  # qlocale_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["breeze-icons", "dbus"]
pkgdesc = "KDE Framework for managing menu and toolbar actions"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kxmlgui/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kxmlgui-{pkgver}.tar.xz"
sha256 = "6d5e240c835668419ac036666fa4c99e3479795c6988100763f810ca8835c401"
hardening = ["vis"]


@subpackage("kxmlgui-devel")
def _(self):
    self.depends += [
        "kconfig-devel",
        "kconfigwidgets-devel",
        "kguiaddons-devel",
    ]

    return self.default_devel()
