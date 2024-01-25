pkgname = "gtk+3"
pkgver = "3.24.41"
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
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "perl",
    "glib-devel",
    "gettext-devel",
    "wayland-progs",
    "xsltproc",
    "docbook-xsl-nons",
]
makedepends = [
    "at-spi2-core-devel",
    "gdk-pixbuf-devel",
    "libepoxy-devel",
    "pango-devel",
    "colord-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "wayland-protocols",
    "mesa-devel",
    "libxcursor-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "libxcomposite-devel",
    "libxi-devel",
    "cups-devel",
    "tracker-devel",
    "libcloudproviders-devel",
    "iso-codes",
]
depends = [
    "adwaita-icon-theme",
    "gtk-update-icon-cache",
    "shared-mime-info",
    "virtual:gdk-pixbuf-loader-svg!librsvg",
]
checkdepends = [
    "weston",
    "dbus",
    "adwaita-icon-theme",
    "librsvg",
    "fonts-dejavu-otf",
]
triggers = ["/usr/lib/gtk-3.0/3.0.0/immodules"]
pkgdesc = "Gimp Toolkit version 3"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gtk.org"
source = f"$(GNOME_SITE)/gtk+/{pkgver[:-3]}/gtk+-{pkgver}.tar.xz"
sha256 = "47da61487af3087a94bc49296fd025ca0bc02f96ef06c556e7c8988bd651b6fa"
# FIXME int
hardening = ["!int"]
# gtk3 can't handle seatless wayland displays; also
# g_log_set_writer_func called multiple times in tests
options = ["!cross", "!check"]


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


@subpackage("gtk+3-cups")
def _cups(self):
    self.pkgdesc = f"{pkgdesc} (CUPS print backend)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "cups"]

    return ["usr/lib/gtk-3.0/3.0.0/printbackends/libprintbackend-cups.so"]
