pkgname = "kde-inotify-survey"
pkgver = "24.12.3"
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
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE inotify limit monitor"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/system/kde-inotify-survey"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kde-inotify-survey-{pkgver}.tar.xz"
sha256 = "6b572a18514a2288512380ccf5ea1dbbad5e85d4a5e4dc7003d32b84337d46a8"
hardening = ["vis"]
# TODO
options = ["!cross"]
