pkgname = "bolt"
pkgver = "0.9.7"
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
sha256 = "593c7e7d0ecebd7b9e2c3efabe33f8fec5501ff02ffd6d8563cfc14a91c31c1c"


def post_install(self):
    self.install_service(self.files_path / "boltd")

    self.install_dir("var/lib/boltd", empty=True)
