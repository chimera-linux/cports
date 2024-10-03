pkgname = "swaync"
pkgver = "0.10.1"
pkgrel = 2
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
pkgdesc = "Notification daemon for sway"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/ErikReider/SwayNotificationCenter"
source = f"https://github.com/ErikReider/SwayNotificationCenter/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5586d8a679dde5e530cb8b6f0c86abdd0d5e41362fc1c4e56e2211edea0f7a13"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_service(self.files_path / "swaync.user")
