pkgname = "gst-plugins-base"
pkgver = "1.24.1"
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
sha256 = "884045d1d7c5d6bb8605e45c7ee0e9f1341888e81c2b7c42dff52bb98ede8ec3"
# FIXME int
hardening = ["!int"]
# FIXME libs_allocators fail
options = ["!cross", "!check"]


@subpackage("gst-plugins-base-devel")
def _devel(self):
    return self.default_devel()
