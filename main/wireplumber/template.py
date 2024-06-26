pkgname = "wireplumber"
pkgver = "0.5.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystem-lua=true",
    "-Ddoc=disabled",
    "-Dintrospection=enabled",
]
hostmakedepends = [
    "doxygen",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-lxml",
]
makedepends = ["pipewire-devel", "glib-devel", "lua5.4-devel"]
checkdepends = ["pipewire", "dbus"]
depends = ["pipewire"]
provides = [f"pipewire-session-manager={pkgver}-r{pkgrel}"]
pkgdesc = "Session and policy manager implementation for PipeWire"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.pages.freedesktop.org/wireplumber"
source = f"https://gitlab.freedesktop.org/pipewire/wireplumber/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "83a75ab7dc88fbce976378fc2303418f8c66a8562120f4f598391ae263d7fc9e"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wireplumber.user", enable=True)


@subpackage("wireplumber-devel")
def _devel(self):
    return self.default_devel()
