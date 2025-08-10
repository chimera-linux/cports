pkgname = "swaync"
pkgver = "0.12.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "meson",
    "pkgconf",
    "sassc",
    "scdoc",
    "vala",
]
makedepends = [
    "granite-devel",
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgee-devel",
    "libhandy-devel",
    "libpulse-devel",
    "wayland-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Notification daemon for sway"
license = "GPL-3.0-or-later"
url = "https://github.com/ErikReider/SwayNotificationCenter"
source = f"https://github.com/ErikReider/SwayNotificationCenter/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8a6475bfdd8abf5be1267ede0a233266b3f14311b169047bde599752a3ac981c"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_service(self.files_path / "swaync.user")
