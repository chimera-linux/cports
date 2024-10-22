pkgname = "plasma-browser-integration"
pkgver = "6.2.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later AND MIT"
url = "https://community.kde.org/Plasma/Browser_Integration"
source = (
    f"$(KDE_SITE)/plasma/{pkgver}/plasma-browser-integration-{pkgver}.tar.xz"
)
sha256 = "6bc4a6b7941c8a0d12d52d167cbb1410a225d43a0f77d353017b2c941e676b0e"
# the MIT one has no attribution in it..
options = ["!distlicense"]
