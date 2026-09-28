pkgname = "icewm"
pkgver = "4.1.0"
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
sha256 = "3ca0e7c29939e0a3d532dbe6e70a1e3b3bd7ce13fa7194a34ae1fe12a7aded32"


def post_install(self):
    # weird buildsystem thing
    self.uninstall("builddir")
