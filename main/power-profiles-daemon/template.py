pkgname = "power-profiles-daemon"
pkgver = "0.21"
pkgrel = 1
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
sha256 = "c61a2350e58d51d4d6e58a61cf2aaa9b307ce42f16c40c4ece0bf1ed6d020506"
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
