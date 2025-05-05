pkgname = "icewm"
pkgver = "3.7.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCONFIG_GDK_PIXBUF_XLIB=ON",
    "-DCONFIG_LIBRSVG=ON",
    "-DCONFIG_XPM=ON",
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
    "libxdamage-devel",
    "libxft-devel",
    "libxinerama-devel",
    "libxpm-devel",
    "libxrandr-devel",
    "libxrender-devel",
]
depends = ["shared-mime-info"]
pkgdesc = "Window manager for X11"
license = "GPL-2.0-or-later"
url = "https://ice-wm.org"
source = f"https://github.com/ice-wm/icewm/archive/{pkgver}.tar.gz"
sha256 = "1e9998edbb79c8c33effc97ebc04f49a072b8327721b406a894d5d2a11912508"


def post_install(self):
    # weird buildsystem thing
    self.uninstall("builddir")
