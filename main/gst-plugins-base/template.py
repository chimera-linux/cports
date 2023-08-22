pkgname = "gst-plugins-base"
pkgver = "1.22.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=disabled",
    "-Dtremor=disabled",
    "-Ddoc=disabled",
    "-Dcdparanoia=enabled",
    "-Dintrospection=enabled",
    "-Ddefault_library=shared",
]
make_check_env = {"XDG_RUNTIME_DIR": "/etc/xdg"}
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext",
    "glib-devel",
    "orc",
    "gobject-introspection",
    "wayland-progs",
]
makedepends = [
    "gstreamer-devel",
    "libxml2-devel",
    "glib-devel",
    "pango-devel",
    "cairo-devel",
    "graphene-devel",
    "libgudev-devel",
    "libvisual-devel",
    "orc-devel",
    "cdparanoia-devel",
    "libtheora-devel",
    "libvorbis-devel",
    "opus-devel",
    "libpng-devel",
    "libjpeg-turbo-devel",
    "mesa-devel",
    "libxv-devel",
    "libxext-devel",
    "libsm-devel",
    "wayland-devel",
    "wayland-protocols",
]
checkdepends = ["mesa-dri", "fonts-liberation-otf"]
depends = ["orc", f"gstreamer~{pkgver}"]
pkgdesc = "GStreamer base plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "edd4338b45c26a9af28c0d35aab964a024c3884ba6f520d8428df04212c8c93a"
# FIXME int
hardening = ["!int"]
# FIXME libs_allocators fail
options = ["!cross", "!check"]


@subpackage("gst-plugins-base-devel")
def _devel(self):
    return self.default_devel()
