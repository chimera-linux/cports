pkgname = "grilo-plugins"
pkgver = "0.3.17"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: libgdata if/when it moves off libsoup2
    # (see https://gitlab.gnome.org/GNOME/libgdata/-/merge_requests/49)
    "-Denable-youtube=no",
]
hostmakedepends = [
    "gettext",
    "gperf",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "avahi-glib-devel",
    "gnome-online-accounts-devel",
    "gom-devel",
    "grilo-devel",
    "gstreamer-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libdmapsharing-devel",
    "libmediaart-devel",
    "liboauth-devel",
    "libsoup-devel",
    "libxml2-devel",
    "lua5.4-devel",
    "rest-devel",
    "sqlite-devel",
    "tinysparql-devel",
    "totem-pl-parser-devel",
]
checkdepends = ["gst-plugins-good"]
pkgdesc = "Collection of plugins for Grilo"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/grilo-plugins"
source = (
    f"$(GNOME_SITE)/grilo-plugins/{pkgver[:-3]}/grilo-plugins-{pkgver}.tar.xz"
)
sha256 = "483c03f2ce06f96d42b85768fdc494c076d58474bf8e3c326f5a050fd4a2f03c"
# FIXME: Two tests fail
options = ["!check"]


@subpackage("grilo-plugins-devel")
def _(self):
    return self.default_devel()
