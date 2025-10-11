pkgname = "swaync"
pkgver = "0.12.2"
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
    "dinit-chimera",
    "dinit-dbus",
    "granite-devel",
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgee-devel",
    "libhandy-devel",
    "libpulse-devel",
    "turnstile",
    "wayland-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Notification daemon for sway"
license = "GPL-3.0-or-later"
url = "https://github.com/ErikReider/SwayNotificationCenter"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c440223f199b4f0d28e2434f879a2ad2103cb6aaac670313434b05926707535e"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_service(self.files_path / "swaync.user")
