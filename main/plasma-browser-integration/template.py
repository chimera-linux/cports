pkgname = "plasma-browser-integration"
pkgver = "6.6.5"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kjobwidgets-devel",
    "knotifications-devel",
    "krunner-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "plasma-activities-devel",
    "plasma-workspace-devel",
    "purpose-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE integration with the system browser"
license = "GPL-3.0-or-later AND MIT"
url = "https://community.kde.org/Plasma/Browser_Integration"
source = (
    f"$(KDE_SITE)/plasma/{pkgver}/plasma-browser-integration-{pkgver}.tar.xz"
)
sha256 = "3c54bf15cd70c48f26bb65e6d787a013a86f2375d8fefd2c0acab650b37846f9"
# the MIT one has no attribution in it..
options = ["!distlicense"]
