pkgname = "bolt"
pkgver = "0.9.9"
pkgrel = 0
build_style = "meson"
# XXX drop libexec
configure_args = [
    "--libexecdir=/usr/lib",
    "-Dman=true",
    "-Dsystemd=false",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "asciidoc",
    "bash",
    "glib-devel",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = ["udev-devel", "glib-devel", "polkit-devel"]
checkdepends = ["dbus"]
depends = ["dinit-dbus"]
pkgdesc = "Thunderbolt device manager"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/bolt/bolt"
source = f"{url}/-/archive/{pkgver}/bolt-{pkgver}.tar.gz"
sha256 = "d2b05e3ee1ffa9b4fc1c4a11138c69bf1f60acba86f07b1b4b40b4d456048936"


def post_install(self):
    self.install_service("^/boltd")
    self.install_tmpfiles("^/tmpfiles.conf")
