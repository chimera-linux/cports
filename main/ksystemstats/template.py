pkgname = "ksystemstats"
pkgver = "6.5.1"
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
sha256 = "2895fa797fe64c1ae586fa1efd1f6e2ee110206e4a73a6ddade69d1cbd013234"
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
