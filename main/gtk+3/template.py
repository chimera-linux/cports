pkgname = "gtk+3"
pkgver = "3.24.30"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dx11_backend=true", "-Dwayland_backend=true", "-Dbroadway_backend=true",
    "-Dprint_backends=file", # TODO: enable cups
    "-Dcolord=yes", # only affects CUPS actually, pre-enable though
    "-Dgtk_doc=false",
    "-Dman=true",
    "-Dintrospection=true",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "perl", "glib-devel",
    "gettext-tiny-devel", "wayland-progs", "xsltproc", "docbook-xsl-nons",
]
makedepends = [
    "at-spi2-atk-devel", "gdk-pixbuf-devel", "libepoxy-devel", "pango-devel",
    "colord-devel", "libxkbcommon-devel", "wayland-devel", "wayland-protocols",
    "mesa-devel", "libxcursor-devel", "libxdamage-devel", "libxext-devel",
    "libxinerama-devel", "libxrandr-devel", "libxcomposite-devel",
    "libxi-devel", "iso-codes",
]
depends = [
    "gtk-update-icon-cache", "adwaita-icon-theme",
    "virtual:gdk-pixbuf-loader-svg"
]
checkdepends = ["xvfb-run", "dbus"] + depends
depends_providers = {
    "virtual:gdk-pixbuf-loader-svg": "gdk-pixbuf-loader-lunasvg"
}
pkgdesc = "Gimp Toolkit (3.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gtk.org"
source = f"$(GNOME_SITE)/gtk+/{pkgver[:-3]}/gtk+-{pkgver}.tar.xz"
sha256 = "ba75bfff320ad1f4cfbee92ba813ec336322cc3c660d406aad014b07087a3ba9"
# a bunch of tests fail, plus unpackaged checkdepends + needs do_check
options = ["!check"]

@subpackage("gtk-update-icon-cache")
def _uic(self):
    self.pkgdesc = f"{pkgdesc} (icon cache update tool)"
    self.triggers = ["/usr/share/icons/*"]

    return [
        "usr/bin/gtk-update-icon-cache",
        "usr/share/man/man1/gtk-update-icon-cache.1",
    ]

@subpackage("gtk+3-devel")
def _devel(self):
    return self.default_devel()

@subpackage("gtk+3-demo")
def _demo(self):
    self.pkgdesc = f"{pkgdesc} (demo applications)"

    return [
        "usr/bin/gtk3-demo",
        "usr/bin/gtk3-widget-factory",
        "usr/bin/gtk3-demo-application",
        "usr/share/man/man1/gtk3-widget-factory.1",
        "usr/share/gtk-3.0/gtkbuilder.rng",
        "usr/share/glib-2.0/schemas/org.gtk.Demo.gschema.xml",
        "usr/share/applications/gtk3-widget-factory.desktop",
        "usr/share/applications/gtk3-demo.desktop",
        "usr/share/icons",
    ]
