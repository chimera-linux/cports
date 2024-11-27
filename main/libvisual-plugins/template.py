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
install_if = [self.with_pkgver("libvisual-plugins-meta")]
pkgdesc = "Plugins for libvisual"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://libvisual.org"
source = f"https://github.com/Libvisual/libvisual/releases/download/libvisual-plugins-{pkgver}/libvisual-plugins-{pkgver}.tar.bz2"
sha256 = "a1dd04eb3d311d68b4f43a5c707df7aba7a98a9cab820c58395a7f5d7d6d0157"


@subpackage("libvisual-plugins-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
