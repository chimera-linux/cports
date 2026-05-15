pkgname = "icewm"
pkgver = "4.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCONFIG_GDK_PIXBUF_XLIB=ON",
    "-DCONFIG_LIBRSVG=ON",
    "-DCFGDIR=/etc/icewm",
    "-DICESOUND=alsa",
    "-DXTERMCMD=urxvt",
]
hostmakedepends = [
    "asciidoc",
    "cmake",
    "gettext",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "fontconfig-devel",
    "fribidi-devel",
    "gdk-pixbuf-devel",
    "imlib2-devel",
    "librsvg-devel",
    "libsm-devel",
    "libsndfile-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxft-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxres-devel",
]
depends = ["shared-mime-info"]
pkgdesc = "Window manager for X11"
license = "GPL-2.0-or-later"
url = "https://ice-wm.org"
source = f"https://github.com/ice-wm/icewm/archive/{pkgver}.tar.gz"
sha256 = "9a2eb74449bf4c2b995fd8b85c392dda06f0da684fae34849d8f04466b2e5943"


def post_install(self):
    # weird buildsystem thing
    self.uninstall("builddir")
