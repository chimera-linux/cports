pkgname = "swaync"
pkgver = "0.11.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "sassc",
    "scdoc",
    "vala",
]
makedepends = [
    "granite-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "json-glib-devel",
    "libhandy-devel",
    "libpulse-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Notification daemon for sway"
license = "GPL-3.0-or-later"
url = "https://github.com/ErikReider/SwayNotificationCenter"
source = f"https://github.com/ErikReider/SwayNotificationCenter/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7f69fe248994404af4115d335929b3bd2faf8c6321374b5b3e3fa2c97d169c90"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_service(self.files_path / "swaync.user")
