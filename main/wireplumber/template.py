pkgname = "wireplumber"
pkgver = "0.5.18"
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
makedepends = [
    "dinit-chimera",
    "dinit-dbus",
    "glib-devel",
    "lua5.4-devel",
    "pipewire-devel",
]
checkdepends = ["pipewire", "dbus"]
depends = ["pipewire"]
provides = [self.with_pkgver("pipewire-session-manager")]
pkgdesc = "Session and policy manager implementation for PipeWire"
license = "MIT"
url = "https://pipewire.pages.freedesktop.org/wireplumber"
source = f"https://gitlab.freedesktop.org/pipewire/wireplumber/-/archive/{pkgver}/wireplumber-{pkgver}.tar.gz"
sha256 = "8c8a326a5b2a570681c1503c83f1fce0cc54ba862019815604b2bc92a7d483a1"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wireplumber.user", enable=True)


@subpackage("wireplumber-devel")
def _(self):
    return self.default_devel()
