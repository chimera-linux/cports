pkgname = "grilo-plugins"
pkgver = "0.3.18"
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
sha256 = "8e3ce74ee717c3c322d0cb0f8df26bb0914028a5d016e28055ffb49cc9a46c5e"
# FIXME: Two tests fail
options = ["!check"]


@subpackage("grilo-plugins-devel")
def _(self):
    return self.default_devel()
