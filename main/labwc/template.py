pkgname = "labwc"
pkgver = "0.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dman-pages=enabled",
    "-Dxwayland=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "libdrm-devel",
    "librsvg-devel",
    "libsfdo-devel",
    "libxcb-devel",
    "libxml2-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.18-devel",
    "xwayland-devel",
]
depends = ["xwayland"]
pkgdesc = "Stacking wayland compositor"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/labwc/labwc"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1adba1c87ec26f2f00409b47a0b79ccfd68bd160e1abc41822fb01f0a76ee947"
