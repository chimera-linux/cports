pkgname = "labwc"
pkgver = "0.8.3"
pkgrel = 1
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
license = "GPL-2.0-only"
url = "https://github.com/labwc/labwc"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "746be2ff2d0c0c0b795c97fa24c7058f75586685c88a1194c243b6a846f938a5"
