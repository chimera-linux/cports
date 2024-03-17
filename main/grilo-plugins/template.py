pkgname = "grilo-plugins"
pkgver = "0.3.16"
pkgrel = 1
build_style = "meson"
configure_args = [
    # TODO: gom
    "-Denable-bookmarks=no",
    "-Denable-thetvdb=no",
    # TODO: libdmapsharing
    "-Denable-dmap=no",
    # TODO: libgdata if/when it moves off libsoup2
    # (see https://gitlab.gnome.org/GNOME/libgdata/-/merge_requests/49)
    "-Denable-youtube=no",
    # TODO: libmediaart
    "-Denable-local-metadata=no",
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
    "grilo-devel",
    "gstreamer-devel",
    "json-glib-devel",
    "liboauth-devel",
    "libsoup-devel",
    "lua5.4-devel",
    "totem-pl-parser-devel",
    "tracker-devel",
]
pkgdesc = "Collection of plugins for Grilo"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/grilo-plugins"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fe6f4dbe586c6b8ba2406394e202f22d009d642a96eb3a54f32f6a21d084cdcb"


@subpackage("grilo-plugins-devel")
def _devel(self):
    return self.default_devel()
