pkgname = "kalarm"
pkgver = "24.12.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_LIBMPV=ON", "-DENABLE_LIBVLC=OFF"]
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://apps.kde.org/kalarm"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kalarm-{pkgver}.tar.xz"
sha256 = "04dff68aab1f271137e64331f9b1c42473a2a6a87ee87c994bd411534aea7326"
