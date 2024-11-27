pkgname = "plasma-browser-integration"
pkgver = "6.2.4"
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
sha256 = "504be1bb0cb22b1a13c0b7471351672fba3a46bdc8e5724d4ba4013e8f2d63cd"
# the MIT one has no attribution in it..
options = ["!distlicense"]
