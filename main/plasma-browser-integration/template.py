pkgname = "plasma-browser-integration"
pkgver = "6.7.0"
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
sha256 = "cd5b483ee2891de6bb062deaeb6afe0c0a29e951e072510c012c15b49b1b954b"
# the MIT one has no attribution in it..
options = ["!distlicense"]
