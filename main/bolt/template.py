pkgname = "bolt"
pkgver = "0.9.8"
pkgrel = 4
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/bolt/bolt"
source = f"{url}/-/archive/{pkgver}/bolt-{pkgver}.tar.gz"
sha256 = "5a4306aa21ee398e1e9f2a5072748c9469c9360bf5edc7dcec2f12fc17be122e"


def post_install(self):
    self.install_service(self.files_path / "boltd")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
