pkgname = "swaync"
pkgver = "0.12.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd-service=false"]
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
sha256 = "0c844eb5c9524f924495bd4145e5db575096de36f3ec87fb37e4c1ed6eacb897"
hardening = ["vis"]
options = ["etcfiles"]


def post_install(self):
    self.install_service(self.files_path / "swaync.user")
