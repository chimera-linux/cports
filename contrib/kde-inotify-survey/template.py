pkgname = "kde-inotify-survey"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kauth-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "knotifications-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["kirigami-addons"]
checkdepends = ["xwayland-run"] + depends
pkgdesc = "KDE inotify limit monitor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/system/kde-inotify-survey"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kde-inotify-survey-{pkgver}.tar.xz"
sha256 = "db9fa5ab6664ab2ee0eafeee5c9667e917d28e1fac02bcce6d2c2529437d79bf"
# CFI: check
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]
