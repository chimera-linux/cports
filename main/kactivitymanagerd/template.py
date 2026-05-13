pkgname = "kactivitymanagerd"
pkgver = "6.6.5"
pkgrel = 0
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
sha256 = "859bb8e7a6efb4210a82512abec4d7b6ea9ac6f883a2b1db4d3de5ca11452224"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
