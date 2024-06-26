pkgname = "ksystemstats"
pkgver = "6.1.1"
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
sha256 = "f207ea4611143ca8f8b6609a89cdf483b5f8b497234e085215631a848c4e2aab"
# silence some ~600 lines of spam...
tool_flags = {"CXXFLAGS": ["-Wno-deprecated-declarations"]}
# FIXME: cfi breaks at least ksystemstatstest in dbusApi() like https://paste.c-net.org/tnqlkafoixrz
hardening = ["vis", "!cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)
