pkgname = "krdp"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
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
sha256 = "71065cb742aeadd36ae24e29c5bf1e883cd084d30fb2394215c589274012b58b"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_service(self.files_path / "krdpserver.user")
