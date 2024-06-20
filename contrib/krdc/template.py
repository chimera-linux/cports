pkgname = "krdc"
pkgver = "24.05.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "freerdp",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
    "kconfig-devel",
    "kcmutils-devel",
    "kdnssd-devel",
    "knotifyconfig-devel",
    "knotifications-devel",
    "kbookmarks-devel",
    "kiconthemes-devel",
    "kxmlgui-devel",
    "kcompletion-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "ki18n-devel",
    "kio-devel",
    "kstatusnotifieritem-devel",
    "plasma-activities-devel",
    "kdoctools-devel",
    "libvncserver-devel",
    "libssh-devel",
    "freerdp-devel",
]
depends = ["freerdp"]
pkgdesc = "KDE remote desktop client"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/krdc"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/krdc-{pkgver}.tar.xz"
sha256 = "8290e2fd2f4aeb4b39b0528372130624c37ab0ddfad09ebe30007170893364b4"


@subpackage("krdc-devel")
def _devel(self):
    return self.default_devel()
