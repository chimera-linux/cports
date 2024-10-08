pkgname = "plasma-browser-integration"
pkgver = "6.2.0"
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
sha256 = "91d596cfd891b44c10c5dd7862e2c95acda7526fe9a9f018e946836c17450a68"
# the MIT one has no attribution in it..
options = ["!distlicense"]
