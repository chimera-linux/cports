pkgname = "labwc"
pkgver = "0.9.5"
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
    "wlroots0.19-devel",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
depends = ["xwayland"]
pkgdesc = "Stacking wayland compositor"
license = "GPL-2.0-only"
url = "https://github.com/labwc/labwc"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "905af63ad24643a6f548b51107a05ac639d1707aaafdd18f656b55f7cfb28611"
