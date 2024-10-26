pkgname = "power-profiles-daemon"
pkgver = "0.23"
pkgrel = 2
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
    "libgudev-devel",
    "polkit-devel",
    "upower-devel",
]
depends = ["dinit-dbus", "!tlp", "python-gobject"]
checkdepends = ["python-dbusmock", "umockdev"]
install_if = [self.with_pkgver("power-profiles-daemon-meta")]
pkgdesc = "D-Bus daemon for power management control"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
source = f"{url}/-/archive/{pkgver}/power-profiles-daemon-{pkgver}.tar.bz2"
sha256 = "a71f79e9cb1c184b7a8e25c3ae70d624ea4313edec3401495992c364b5f22599"
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
