pkgname = "konversation"
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
    "karchive-devel",
    "kbookmarks-devel",
    "kcodecs-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kidletime-devel",
    "kio-devel",
    "kitemviews-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kparts-devel",
    "kstatusnotifieritem-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "qca-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE IRC client"
license = "GPL-3.0-only"
url = "https://konversation.kde.org"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/konversation-{pkgver}.tar.xz"
)
sha256 = "3b6e0d6b0bbf055893780a18026eef682ccffe44df2580d923089a0acedc220c"
