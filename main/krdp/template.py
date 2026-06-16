pkgname = "krdp"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "freerdp",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "dinit-dbus-dinit",
    "freerdp-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kpipewire-devel",
    "kstatusnotifieritem-devel",
    "linux-pam-devel",
    "plasma-wayland-protocols",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
    "turnstile",
]
pkgdesc = "KDE RDP server library and examples"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/krdp"
source = f"$(KDE_SITE)/plasma/{'.'.join(pkgver.split('.')[0:3])}/krdp-{pkgver}.tar.xz"
sha256 = "e65ca56cf2f966994510dccecd53892922e261ad7dba9911d2f374060293c6db"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_service(self.files_path / "krdpserver.user")
