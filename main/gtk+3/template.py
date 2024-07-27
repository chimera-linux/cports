pkgname = "gtk+3"
pkgver = "3.24.43"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbroadway_backend=true",
    "-Dcloudproviders=true",
    "-Dcolord=yes",
    "-Dgtk_doc=false",
    "-Dintrospection=true",
    "-Dman=true",
    "-Dprint_backends=cups,file",
    "-Dtests=false",
    "-Dtracker3=true",
    "-Dwayland_backend=true",
    "-Dx11_backend=true",
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "perl",
    "pkgconf",
    "wayland-progs",
    "xsltproc",
]
makedepends = [
    "at-spi2-core-devel",
    "colord-devel",
    "cups-devel",
    "gdk-pixbuf-devel",
    "iso-codes",
    "libcloudproviders-devel",
    "libepoxy-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "mesa-devel",
    "pango-devel",
    "tracker-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = [
    "adwaita-icon-theme",
    "gtk-update-icon-cache",
    "shared-mime-info",
    "virtual:gdk-pixbuf-loader-svg!librsvg",
]
checkdepends = [
    "adwaita-icon-theme",
    "dbus",
    "fonts-dejavu-otf",
    "librsvg",
    "xwayland-run",
]
triggers = ["/usr/lib/gtk-3.0/3.0.0/immodules"]
pkgdesc = "Gimp Toolkit version 3"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gtk.org"
source = f"$(GNOME_SITE)/gtk+/{pkgver[:-3]}/gtk+-{pkgver}.tar.xz"
sha256 = "7e04f0648515034b806b74ae5d774d87cffb1a2a96c468cb5be476d51bf2f3c7"
# FIXME int
hardening = ["!int"]
# gtk3 can't handle seatless wayland displays; also
# g_log_set_writer_func called multiple times in tests
options = ["!cross", "!check"]


@subpackage("gtk-update-icon-cache")
def _uic(self):
    self.subdesc = "icon cache update tool"
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
    self.subdesc = "demo applications"

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


@subpackage("gtk+3-cups")
def _cups(self):
    self.subdesc = "CUPS print backend"
    self.install_if = [self.parent, "cups"]

    return ["usr/lib/gtk-3.0/3.0.0/printbackends/libprintbackend-cups.so"]
