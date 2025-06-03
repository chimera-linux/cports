pkgname = "gst-plugins-base"
pkgver = "1.26.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddefault_library=shared",
    # stuff we don't want
    # use pulse
    "-Dalsa=disabled",
    # scuffed vorbis decoder
    "-Dtremor=disabled",
    # misc
    "-Ddoc=disabled",
    "-Dexamples=disabled",
]
make_check_args = ["--timeout-multiplier=5"]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "orc",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "cdparanoia-devel",
    "glib-devel",
    "graphene-devel",
    "gstreamer-devel",
    "iso-codes",
    "libgudev-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libsm-devel",
    "libtheora-devel",
    "libvisual-devel",
    "libvorbis-devel",
    "libxext-devel",
    "libxi-devel",
    "libxml2-devel",
    "libxv-devel",
    "mesa-devel",
    "opus-devel",
    "orc-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = [
    f"gstreamer~{pkgver}",
    "libvisual-plugins-meta",
    "orc",
]
checkdepends = ["fonts-liberation-otf"]
pkgdesc = "GStreamer base plugins"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-plugins-base/gst-plugins-base-{pkgver}.tar.xz"
sha256 = "f4b9fc0be852fe5f65401d18ae6218e4aea3ff7a3c9f8d265939b9c4704915f7"
# FIXME int
hardening = ["!int"]
# gobject-introspection
options = ["!cross"]


@subpackage("gst-plugins-base-devel")
def _(self):
    return self.default_devel()
