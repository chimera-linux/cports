pkgname = "icewm"
pkgver = "3.7.5"
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
sha256 = "ffcaa0eb86af022edbf8b3ad7d57c6c20125a64f678cf451a0665d891a4683e0"


def post_install(self):
    # weird buildsystem thing
    self.uninstall("builddir")
