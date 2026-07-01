pkgname = "labwc"
pkgver = "0.20.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dman-pages=enabled",
    "-Dxwayland=enabled",
]
hostmakedepends = [
    "gettext",
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
    "wlroots0.20-devel",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
depends = ["xwayland"]
pkgdesc = "Stacking wayland compositor"
license = "GPL-2.0-only"
url = "https://github.com/labwc/labwc"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2c95d8c19cc50ce0dd5cf3e412932ebb4d3353bc4a5d11e2405d124e6c77dcd2"
