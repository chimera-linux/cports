pkgname = "khelpcenter"
pkgver = "24.08.1"
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
    "karchive-devel",
    "kbookmarks-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kservice-devel",
    "ktexttemplate-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwebengine-devel",
    "xapian-core-devel",
]
checkdepends = ["perl"]
pkgdesc = "KDE application documentation viewer"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/khelpcenter"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/khelpcenter-{pkgver}.tar.xz"
sha256 = "760fa25a57b942ba53265a56ffb12649ff9f594dcdfc67dadfd9bc51c1287e7c"
