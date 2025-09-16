pkgname = "bolt"
pkgver = "0.9.10"
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
makedepends = [
    "dinit-chimera",
    "glib-devel",
    "polkit-devel",
    "udev-devel",
]
checkdepends = ["dbus"]
depends = ["dinit-dbus"]
pkgdesc = "Thunderbolt device manager"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/bolt/bolt"
source = f"{url}/-/archive/{pkgver}/bolt-{pkgver}.tar.gz"
sha256 = "0e9646ff153f4445d85bfaac1b0d77d86df9c639f84888f15ee7b0f1fa892b58"


def post_install(self):
    self.install_service("^/boltd")
    self.install_tmpfiles("^/tmpfiles.conf")
