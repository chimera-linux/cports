pkgname = "ksystemstats"
pkgver = "6.2.4"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "elogind-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "libksysguard-devel",
    "libnl-devel",
    "libsensors-devel",
    "networkmanager-qt-devel",
    "qt6-qtdeclarative-devel",
    "solid-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Plugin based system monitoring daemon"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/ksystemstats"
source = f"$(KDE_SITE)/plasma/{pkgver}/ksystemstats-{pkgver}.tar.xz"
sha256 = "49a94ef05e6ab0e8f0ff5a272194f34d8a4d572fe79fcab65c96ea2ec1460c43"
# silence some ~600 lines of spam...
tool_flags = {"CXXFLAGS": ["-Wno-deprecated-declarations"]}
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
