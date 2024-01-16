pkgname = "wireplumber"
pkgver = "0.4.17"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystem-lua=true",
    "-Ddoc=disabled",
    "-Dintrospection=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "python-lxml",
    "glib-devel",
    "doxygen",
]
makedepends = ["pipewire-devel", "glib-devel", "lua5.4-devel"]
checkdepends = ["pipewire", "dbus"]
provides = [f"pipewire-session-manager={pkgver}-r{pkgrel}"]
pkgdesc = "Session and policy manager implementation for PipeWire"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pipewire.pages.freedesktop.org/wireplumber"
source = f"https://gitlab.freedesktop.org/pipewire/wireplumber/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a12534fd9c1ecf9fbc09f79192d9d57c9ab7bf01da82615ab4103b2f8e2e91a7"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "wireplumber.user", enable=True)


@subpackage("wireplumber-devel")
def _devel(self):
    return self.default_devel()
