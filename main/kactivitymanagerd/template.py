pkgname = "kactivitymanagerd"
pkgver = "6.6.4"
pkgrel = 1
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "boost-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
# depends = ["qt6-qtbase-sql"]
pkgdesc = "KDE Manage user's activities and track usage patterns"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/kactivitymanagerd"
source = f"$(KDE_SITE)/plasma/{pkgver}/kactivitymanagerd-{pkgver}.tar.xz"
sha256 = "b405af0c48ad47ee4f2c70fd2a2aef9eee521120c15cac3f78945bd0e0fb3166"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
