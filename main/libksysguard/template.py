pkgname = "libksysguard"
pkgver = "6.4.5"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libcap-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kauth-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "knewstuff-devel",
    "kpackage-devel",
    "kservice-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libcap-devel",
    "libnl-devel",
    "libpcap-devel",
    "lm-sensors-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE system monitor library"
license = "LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/plasma/libksysguard/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/libksysguard-{pkgver}.tar.xz"
sha256 = "c7cf8cd2f0a1e519201dc62889f1135967a850f932c252fd26ea3d88c6564a0f"
file_modes = {
    "usr/lib/ksysguard/ksgrd_network_helper": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/lib/ksysguard/ksgrd_network_helper": {
        "security.capability": "cap_net_raw+ep",
    },
}
hardening = ["vis"]


@subpackage("libksysguard-devel")
def _(self):
    return self.default_devel()
