pkgname = "labwc"
pkgver = "0.8.1"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://github.com/labwc/labwc"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8e510655cf0c84875c541f4afeb636e707d365210993ad22d64d8bc3108a3433"
