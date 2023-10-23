pkgname = "icewm"
pkgver = "3.4.3"
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
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext", "asciidoc", "perl"]
makedepends = [
    "alsa-lib-devel",
    "fontconfig-devel",
    "gdk-pixbuf-devel",
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
    "fribidi-devel",
    "imlib2-devel",
]
depends = ["shared-mime-info"]
pkgdesc = "Window manager for X11"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://ice-wm.org"
source = f"https://github.com/ice-wm/icewm/archive/{pkgver}.tar.gz"
sha256 = "3eab580609f22a103c4014ce7eb857f27e1728175138f2d39808d672dd9c6d81"
