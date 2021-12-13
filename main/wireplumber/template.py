pkgname = "wireplumber"
pkgver = "0.4.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystem-lua=true", "-Ddoc=disabled", "-Dintrospection=enabled"
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "python-lxml", "glib-devel",
    "doxygen"
]
makedepends = [
    "pipewire-devel", "libglib-devel", "lua5.4-devel"
]
checkdepends = ["pipewire", "dbus"]
install_if = ["pipewire"]
pkgdesc = "Session and policy manager implementation for PipeWire"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.pages.freedesktop.org/wireplumber"
source = f"https://gitlab.freedesktop.org/pipewire/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "73c76c8cd60d3f96e586122a13257586396d7e34b2f9ffad39d27015a1fa0a13"

def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wireplumber.user")

@subpackage("wireplumber-static")
def _static(self):
    return self.default_static()

@subpackage("wireplumber-devel")
def _devel(self):
    return self.default_devel()
