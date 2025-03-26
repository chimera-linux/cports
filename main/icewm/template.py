pkgname = "icewm"
pkgver = "3.7.2"
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
sha256 = "855e2503c16bdf6cb23c2032b9ab3b19a48ca882951d48af7c3258bb7c71214b"
