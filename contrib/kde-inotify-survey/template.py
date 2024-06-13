pkgname = "kde-inotify-survey"
pkgver = "24.05.1"
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
sha256 = "f5a09d8ee03a0b5123eed19803bce4f9e1b98c3a0e079031209ee02633b32c82"
# CFI: check
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]
