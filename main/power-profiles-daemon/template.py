pkgname = "power-profiles-daemon"
pkgver = "0.20"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemdsystemunitdir=", "-Dtests=false"]
hostmakedepends = [
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "libgudev-devel",
    "polkit-devel",
    "upower-devel",
]
depends = ["!tlp", "python-gobject"]
install_if = [f"power-profiles-daemon-meta={pkgver}-r{pkgrel}"]
pkgdesc = "D-Bus daemon for power management control"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "24a0bf1a3012c4f49fbe146fed6bce9fbb7b20c92e4123690ff727a376cc3b6c"
hardening = ["vis"]
# TODO: fix checks
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_dir("var/lib/power-profiles-daemon", empty=True)
    self.install_service(self.files_path / "power-profiles-daemon")


@subpackage("power-profiles-daemon-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.options = ["empty"]
    return []
