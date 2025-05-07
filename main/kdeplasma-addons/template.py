pkgname = "kdeplasma-addons"
pkgver = "6.3.5"
pkgrel = 0
build_style = "cmake"
# FIXME: failed tz comparison / scientific notation number e uppercase
make_check_args = ["-E", "(converterrunnertest|datetimerunnertest)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "kglobalaccel-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kitemmodels-devel",
    "kjobwidgets-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "krunner-devel",
    "kservice-devel",
    "kunitconversion-devel",
    "kxmlgui-devel",
    "libplasma-devel",
    "plasma5support-devel",
    "purpose-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtquick3d-devel",
    "sonnet-devel",
]
depends = [
    "kirigami-addons",
    "kitemmodels",
    "purpose",
    "qt6-qtquick3d",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Plasma addons"
license = "GPL-3.0-only AND CC0-1.0 AND LGPL-3.0-or-later"
url = "https://invent.kde.org/plasma/kdeplasma-addons"
source = f"$(KDE_SITE)/plasma/{pkgver}/kdeplasma-addons-{pkgver}.tar.xz"
sha256 = "27bc430a2d4f5ff85b02c120c45afe3e02287e5b13bd730eabb8ed484d5ea4ba"

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]


@subpackage("kdeplasma-addons-devel")
def _(self):
    return self.default_devel()
