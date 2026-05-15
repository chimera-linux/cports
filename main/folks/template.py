pkgname = "folks"
pkgver = "0.15.12"
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
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Folks"
source = f"$(GNOME_SITE)/folks/{'.'.join(pkgver.split('.')[:2])}/folks-{pkgver}.tar.xz"
sha256 = "21f44e2bdabb1ee7f8e41bb996d10ac7daf35c78c498177db0c00f580a20a914"
tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
# TODO
options = ["!check", "!cross"]


@subpackage("folks-devel")
def _(self):
    return self.default_devel()
