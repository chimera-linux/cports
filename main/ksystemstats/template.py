pkgname = "ksystemstats"
pkgver = "6.2.2"
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
sha256 = "db3afa4bd8ab74c60351a85caf19e5c0b0095a388a24b47d3a957283d85ddffb"
# silence some ~600 lines of spam...
tool_flags = {"CXXFLAGS": ["-Wno-deprecated-declarations"]}
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
