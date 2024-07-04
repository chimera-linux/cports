pkgname = "powerdevil"
pkgver = "6.1.2"
pkgrel = 0
build_style = "cmake"
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
    "kxmlgui-devel",
    "layer-shell-qt-devel",
    "libcap-devel",
    "libkscreen-devel",
    "plasma-activities-devel",
    "plasma-workspace-devel",
    "qt6-qtbase-devel",
]
checkdepends = [
    "bash",
]
depends = [
    "upower",
]
pkgdesc = "KDE Plasma shell power consumption settings manager"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/powerdevil"
source = f"$(KDE_SITE)/plasma/{pkgver}/powerdevil-{pkgver}.tar.xz"
sha256 = "d4a8b85536f69e223697bd1c7abd1dc3fc283a71c5b5cc09a91a247d85d85014"
file_modes = {
    "usr/libexec/org_kde_powerdevil": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/libexec/org_kde_powerdevil": {
        "security.capability": "cap_wake_alarm+ep",
    },
}
hardening = ["vis", "cfi"]


def post_install(self):
    # TODO: dinit user services with graphical
    self.uninstall("usr/lib/systemd/user")
