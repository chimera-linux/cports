pkgname = "power-profiles-daemon"
pkgver = "0.22"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemdsystemunitdir=",
    "-Dzshcomp=/usr/share/zsh/site-functions",
]
hostmakedepends = [
    "glib-devel",
    "meson",
    "pkgconf",
    "python-gobject",
    "python-shtab",
]
makedepends = [
    "libgudev-devel",
    "polkit-devel",
    "upower-devel",
]
depends = ["!tlp", "python-gobject"]
checkdepends = ["python-dbusmock", "umockdev"]
install_if = [self.with_pkgver("power-profiles-daemon-meta")]
pkgdesc = "D-Bus daemon for power management control"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
source = f"{url}/-/archive/{pkgver}/power-profiles-daemon-{pkgver}.tar.bz2"
sha256 = "a030b25c4e86faab782a134cf7ac8e19d1e7edf2d2c0ed6f158750de10c1f8d5"
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    self.install_dir("var/lib/power-profiles-daemon", empty=True)
    self.install_service(self.files_path / "power-profiles-daemon")


@subpackage("power-profiles-daemon-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
