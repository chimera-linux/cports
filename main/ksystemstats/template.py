pkgname = "ksystemstats"
pkgver = "6.6.1"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# appended to below
make_check_args = []
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libcap-progs",
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
    "libcap-devel",
    "libksysguard-devel",
    "libnl-devel",
    "lm-sensors-devel",
    "networkmanager-qt-devel",
    "qt6-qtdeclarative-devel",
    "solid-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Plugin based system monitoring daemon"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/ksystemstats"
source = f"$(KDE_SITE)/plasma/{pkgver}/ksystemstats-{pkgver}.tar.xz"
sha256 = "b08db492c1b7ff984c45f12bdaa73959996923958d85c8e9edd4c9b25547fd73"
# silence some ~600 lines of spam...
tool_flags = {"CXXFLAGS": ["-Wno-deprecated-declarations"]}
file_modes = {
    "usr/lib/ksystemstats_intel_helper": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/lib/ksystemstats_intel_helper": {
        "security.capability": "cap_perfmon+ep",
    },
}
hardening = ["vis"]


if self.profile().arch == "ppc64le":
    make_check_args += [
        "-E",
        "TestLinuxCpu",  # "Subprocess aborted"?
    ]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
