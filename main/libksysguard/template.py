pkgname = "libksysguard"
pkgver = "6.4.4"
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
sha256 = "f12fd2e11d2d504d57556cb520a442ed9660f59c7d4b1fbbb17bee02eba0fb2f"
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
