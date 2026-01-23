pkgname = "powerdevil"
pkgver = "6.5.5"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# FIXME: all tests broken like on alpine, migrateconfig_test*
make_check_args = [
    "-E",
    "(default_configs_can_suspend_to_ram"
    "|activities$"
    "|activities_no_double_migration"
    "|profiles$"
    "|profiles_more)",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libcap-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ddcutil-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kidletime-devel",
    "kio-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "krunner-devel",
    "kxmlgui-devel",
    "libcap-devel",
    "libkscreen-devel",
    "libplasma-devel",
    "plasma-activities-devel",
    "plasma-wayland-protocols",
    "plasma-workspace-devel",
    "qcoro-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtwayland-devel",
]
checkdepends = [
    "bash",
]
depends = [
    "upower",
]
# locale file conflicts ~6.2.3
replaces = ["plasma-workspace<6.2.3"]
pkgdesc = "KDE Plasma shell power consumption settings manager"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/powerdevil"
source = f"$(KDE_SITE)/plasma/{pkgver}/powerdevil-{pkgver}.tar.xz"
sha256 = "1f67c14d05df9cdf86571dd86c33ad91e855e5595cabab7f42289bf7e35ebfe4"
file_modes = {
    "usr/lib/org_kde_powerdevil": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/lib/org_kde_powerdevil": {
        "security.capability": "cap_wake_alarm+ep",
    },
}
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user services with graphical
    self.uninstall("usr/lib/systemd/user")
