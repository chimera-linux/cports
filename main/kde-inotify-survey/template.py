pkgname = "kde-inotify-survey"
pkgver = "24.12.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/system/kde-inotify-survey"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kde-inotify-survey-{pkgver}.tar.xz"
sha256 = "3933e5363ef2e5f118d8858905d5c5357d7a62f89e1f1549b9e8d8b5f52c8d7d"
hardening = ["vis"]
# TODO
options = ["!cross"]
