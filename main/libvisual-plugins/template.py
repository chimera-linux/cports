pkgname = "libvisual-plugins"
pkgver = "0.4.2"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-alsa",
    # cycle
    "--disable-jack",
    "--disable-portaudio",
    "--enable-gdkpixbuf-plugin",
    "--enable-gstreamer-plugin",
    "--enable-opengl",
    "--enable-pulseaudio",
]
hostmakedepends = [
    "automake",
    "bison",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glu-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libpulse-devel",
    "libvisual-devel",
]
install_if = [f"libvisual-plugins-meta={pkgver}-r{pkgrel}"]
pkgdesc = "Abstraction library for audio visualization plugins (plugins)"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "http://libvisual.org"
source = f"https://github.com/Libvisual/libvisual/releases/download/libvisual-plugins-{pkgver}/libvisual-plugins-{pkgver}.tar.bz2"
sha256 = "a1dd04eb3d311d68b4f43a5c707df7aba7a98a9cab820c58395a7f5d7d6d0157"


@subpackage("libvisual-plugins-meta")
def _meta(self):
    self.pkgdesc = f"{pkgdesc} (recommends package)"
    self.options = ["empty"]
    return []
