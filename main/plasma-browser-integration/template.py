pkgname = "plasma-browser-integration"
pkgver = "6.5.2"
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
sha256 = "815b48314af04aabe782125ef9ebade7d50879da9ee3bd7edb23849cda6602ab"
# the MIT one has no attribution in it..
options = ["!distlicense"]
