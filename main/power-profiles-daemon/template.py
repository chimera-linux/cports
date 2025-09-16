pkgname = "power-profiles-daemon"
pkgver = "0.30"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
    "bash-completion",
    "dinit-chimera",
    "dinit-dbus",
    "libgudev-devel",
    "polkit-devel",
    "upower-devel",
]
depends = ["dinit-dbus", "python-gobject"]
checkdepends = ["python-dbusmock", "umockdev"]
install_if = [self.with_pkgver("power-profiles-daemon-meta")]
pkgdesc = "D-Bus daemon for power management control"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
source = f"{url}/-/archive/{pkgver}/power-profiles-daemon-{pkgver}.tar.bz2"
sha256 = "528ee5b8ca0a27d8d66128ebf850e23be9571dc130cf2a82dd2463dac7d3a92f"
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "power-profiles-daemon")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("power-profiles-daemon-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
