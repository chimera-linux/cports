pkgname = "icewm"
pkgver = "3.6.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://ice-wm.org"
source = f"https://github.com/ice-wm/icewm/archive/{pkgver}.tar.gz"
sha256 = "0fa15f252983d21b1bc434142c787b16bdfc347a83c3057586d0e0091f26617b"
