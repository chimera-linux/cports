pkgname = "power-profiles-daemon"
pkgver = "0.13"
pkgrel = 2
build_style = "meson"
configure_args = ["-Dsystemdsystemunitdir=/tmp"]
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
url = "https://gitlab.freedesktop.org/hadess/power-profiles-daemon"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "9fef0a3e1b76e6c0f551841d4a9fef36e6aae047d5279cfc60b833d80fd2a8b7"
hardening = ["vis"]


def post_install(self):
    self.rm(self.destdir / "tmp", recursive=True)
    self.install_license("COPYING")
    self.install_dir("var/lib/power-profiles-daemon", empty=True)
    self.install_service(self.files_path / "power-profiles-daemon")


@subpackage("power-profiles-daemon-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.options = ["empty"]
    return []
