pkgname = "clutter"
pkgver = "1.26.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-examples", "--disable-wayland-backend"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "cogl-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libgudev-devel",
    "libinput-devel",
    "libinput-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxi-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
]
pkgdesc = "Deprecated graphical user interface library"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/Archive/clutter"
source = f"$(GNOME_SITE)/clutter/{pkgver[:-2]}/clutter-{pkgver}.tar.xz"
sha256 = "8b48fac159843f556d0a6be3dbfc6b083fc6d9c58a20a49a6b4919ab4263c4e6"
# TODO: Clutter fails to initialise
options = ["!check", "!cross"]


@subpackage("clutter-devel")
def _(self):
    return self.default_devel()
