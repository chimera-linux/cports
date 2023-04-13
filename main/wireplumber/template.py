pkgname = "wireplumber"
pkgver = "0.4.14"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dsystem-lua=true", "-Ddoc=disabled", "-Dintrospection=enabled"
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "python-lxml", "glib-devel",
    "doxygen"
]
makedepends = [
    "pipewire-devel", "glib-devel", "lua5.4-devel"
]
checkdepends = ["pipewire", "dbus"]
pkgdesc = "Session and policy manager implementation for PipeWire"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.pages.freedesktop.org/wireplumber"
source = f"https://gitlab.freedesktop.org/pipewire/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "b160424ce7c3eeeccba388726f6a448f53501d25085e5fa1bf6c690c1bcd85ea"

def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wireplumber.user")

@subpackage("wireplumber-devel")
def _devel(self):
    return self.default_devel()
