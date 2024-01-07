pkgname = "bolt"
pkgver = "0.9.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dman=true", "-Dsystemd=false"]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "asciidoc",
    "bash",
    "libxml2-progs",
]
makedepends = ["udev-devel", "glib-devel", "polkit-devel"]
checkdepends = ["dbus"]
pkgdesc = "Thunderbolt device manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/bolt/bolt"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "87b442645e8dc06bc4cb3718b6ba8bff6e91401f642aeff83cc4274d633b38fe"


def post_install(self):
    self.install_service(self.files_path / "boltd")

    self.install_dir("var/lib/boltd", empty=True)
