pkgname = "kalarm"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib",  # XXX drop libexec
    "-DENABLE_LIBMPV=ON",
    "-DENABLE_LIBVLC=OFF",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-mime-devel",
    "kauth-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcodecs-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcontacts-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kjobwidgets-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "ktextaddons-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libcanberra-devel",
    "mpv-devel",
    "qt6-qtbase-devel",
]
depends = ["kdepim-runtime"]
pkgdesc = "KDE personal alarm scheduler"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://apps.kde.org/kalarm"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kalarm-{pkgver}.tar.xz"
sha256 = "665504ae5e6b8ce70a0ddc0fa1c972827edd6b5e868066d4990a1466daa8fe0d"
