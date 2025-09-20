pkgname = "wireplumber"
pkgver = "0.5.11"
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
renames = ["pipewire-session-manager"]
pkgdesc = "Session and policy manager implementation for PipeWire"
license = "MIT"
url = "https://pipewire.pages.freedesktop.org/wireplumber"
source = f"https://gitlab.freedesktop.org/pipewire/wireplumber/-/archive/{pkgver}/wireplumber-{pkgver}.tar.gz"
sha256 = "6edd0732741eec2a59a3ffa7d3fe0fc7dbf16dbdf6c38a9cdb977d7491e6008e"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wireplumber.user", enable=True)


@subpackage("wireplumber-devel")
def _(self):
    return self.default_devel()
