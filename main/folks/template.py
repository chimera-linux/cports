pkgname = "folks"
pkgver = "0.15.9"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dtelepathy_backend=false",
    # Needs readline
    "-Dinspect_tool=false",
    "-Dtests=false",
]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "evolution-data-server-devel",
    "glib-devel",
    "libgee-devel",
    "libxml2-devel",
]
checkdepends = ["bluez", "python-dbusmock"]
pkgdesc = "GObject Library to aggregate people into metacontacts"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Folks"
source = f"$(GNOME_SITE)/folks/{'.'.join(pkgver.split('.')[:2])}/folks-{pkgver}.tar.xz"
sha256 = "2311b37355c351f33f163fdc394874a22a0a0682c319493d6d8a6e420711415f"
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# TODO
options = ["!check", "!cross"]


@subpackage("folks-devel")
def _devel(self):
    return self.default_devel()
