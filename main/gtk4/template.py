pkgname = "gtk4"
pkgver = "4.6.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dman-pages=true", "-Dbuild-tests=false", "-Dgtk_doc=false",
    "-Dbroadway-backend=true", "-Dx11-backend=true", "-Dwayland-backend=true",
    "-Dintrospection=enabled", "-Dcolord=enabled", "-Dvulkan=enabled",
    "-Dcloudproviders=disabled",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "perl", "glib-devel",
    "gettext-tiny-devel", "wayland-progs", "wayland-protocols", "xsltproc",
    "docbook-xsl-nons", "python-docutils", "sassc", "gtk-update-icon-cache",
]
makedepends = [
    "at-spi2-atk-devel", "gdk-pixbuf-devel", "libepoxy-devel", "pango-devel",
    "colord-devel", "libxkbcommon-devel", "wayland-devel", "wayland-protocols",
    "mesa-devel", "libxcursor-devel", "libxdamage-devel", "libxext-devel",
    "libxinerama-devel", "libxrandr-devel", "libxcomposite-devel",
    "libxi-devel", "vulkan-loader", "vulkan-headers", "cups-devel",
    "graphene-devel", "gst-plugins-bad-devel", "ffmpeg-devel", "iso-codes",
]
depends = [
    "gtk-update-icon-cache", "adwaita-icon-theme",
    "virtual:gdk-pixbuf-loader-svg!librsvg"
]
pkgdesc = "Gimp Toolkit version 4"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gtk.org"
source = f"$(GNOME_SITE)/gtk/{pkgver[:-2]}/gtk-{pkgver}.tar.xz"
sha256 = "782d5951fbfd585fc9ec76c09d07e28e6014c72db001fb567fff217fb96e4d8c"

def post_install(self):
    # we don't really need it (provided by gtk3)
    self.rm(self.destdir / "usr/bin/gtk4-update-icon-cache")
    self.rm(self.destdir / "usr/share/man/man1/gtk4-update-icon-cache.1")

@subpackage("gtk4-devel")
def _devel(self):
    self.depends += ["vulkan-headers"]

    return self.default_devel()

@subpackage("gtk4-demo")
def _demo(self):
    self.pkgdesc = f"{pkgdesc} (demo applications)"

    return [
        "usr/bin/gtk4-demo",
        "usr/bin/gtk4-widget-factory",
        "usr/bin/gtk4-demo-application",
        "usr/share/man/man1/gtk4-demo.1",
        "usr/share/man/man1/gtk4-widget-factory.1",
        "usr/share/man/man1/gtk4-demo-application.1",
        "usr/share/gtk-4.0/gtk4builder.rng",
        "usr/share/glib-2.0/schemas/org.gtk.Demo4.gschema.xml",
        "usr/share/applications/org.gtk.Demo4.desktop",
        "usr/share/applications/org.gtk.PrintEditor4.desktop",
        "usr/share/applications/org.gtk.WidgetFactory4.desktop",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.Demo4.svg",
        "usr/share/icons/hicolor/symbolic/apps/org.gtk.Demo4-symbolic.svg",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.PrintEditor4.svg",
        "usr/share/icons/hicolor/symbolic/apps/org.gtk.PrintEditor4-symbolic.svg",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.PrintEditor4.Devel.svg",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.WidgetFactory4.svg",
        "usr/share/icons/hicolor/symbolic/apps/org.gtk.WidgetFactory4-symbolic.svg",
    ]

@subpackage("gtk4-cups")
def _cups(self):
    self.pkgdesc = f"{pkgdesc} (CUPS print backend)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "cups"]

    return ["usr/lib/gtk-4.0/4.0.0/printbackends/libprintbackend-cups.so"]
