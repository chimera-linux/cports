pkgname = "wireplumber"
pkgver = "0.4.9"
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
sha256 = "0b25774a2821286a1fa31afb7db8db0573f493b35c40a7031b6e5a30cec0bbe3"

def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wireplumber.user")

@subpackage("wireplumber-devel")
def _devel(self):
    return self.default_devel()
