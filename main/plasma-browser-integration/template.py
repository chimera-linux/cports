pkgname = "plasma-browser-integration"
pkgver = "6.4.1"
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
    "kio-devel",
    "ki18n-devel",
    "kcoreaddons-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "knotifications-devel",
    "plasma-activities-devel",
    "kitemmodels-devel",
    "krunner-devel",
    "purpose-devel",
    "kfilemetadata-devel",
    "plasma-workspace-devel",
    "kjobwidgets-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE integration with the system browser"
license = "GPL-3.0-or-later AND MIT"
url = "https://community.kde.org/Plasma/Browser_Integration"
source = (
    f"$(KDE_SITE)/plasma/{pkgver}/plasma-browser-integration-{pkgver}.tar.xz"
)
sha256 = "7aa0d8c0c722e9f763baef5c153a7f882f490dbcf99563d04727b759c5c2d634"
# the MIT one has no attribution in it..
options = ["!distlicense"]
