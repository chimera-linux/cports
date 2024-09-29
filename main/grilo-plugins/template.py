pkgname = "grilo-plugins"
pkgver = "0.3.16"
pkgrel = 3
build_style = "meson"
configure_args = [
    # TODO: libgdata if/when it moves off libsoup2
    # (see https://gitlab.gnome.org/GNOME/libgdata/-/merge_requests/49)
    "-Denable-youtube=no",
    # enable if/when this moves off libsoup2
    "-Denable-opensubtitles=no",
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
    "sqlite-devel",
    "totem-pl-parser-devel",
    "tinysparql-devel",
]
checkdepends = ["gst-plugins-good"]
pkgdesc = "Collection of plugins for Grilo"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/grilo-plugins"
source = (
    f"$(GNOME_SITE)/grilo-plugins/{pkgver[:-3]}/grilo-plugins-{pkgver}.tar.xz"
)
sha256 = "fe6f4dbe586c6b8ba2406394e202f22d009d642a96eb3a54f32f6a21d084cdcb"
# FIXME: Two tests fail
options = ["!check"]


@subpackage("grilo-plugins-devel")
def _(self):
    return self.default_devel()
