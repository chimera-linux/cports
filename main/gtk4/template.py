pkgname = "gtk4"
pkgver = "4.14.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dman-pages=true",
    "-Dbuild-tests=false",
    "-Dbuild-testsuite=false",
    "-Dgtk_doc=false",
    "-Dbroadway-backend=true",
    "-Dx11-backend=true",
    "-Dwayland-backend=true",
    "-Dintrospection=enabled",
    "-Dcolord=enabled",
    "-Dvulkan=enabled",
    "-Dcloudproviders=enabled",
    "-Dtracker=enabled",
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-update-icon-cache",
    "meson",
    "perl",
    "pkgconf",
    "python-docutils",
    "sassc",
    "shaderc-progs",
    "wayland-progs",
    "wayland-protocols",
    "xsltproc",
]
makedepends = [
    "at-spi2-core-devel",
    "colord-devel",
    "cups-devel",
    "ffmpeg-devel",
    "gdk-pixbuf-devel",
    "graphene-devel",
    "gst-plugins-bad-devel",
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
    "vulkan-headers",
    "vulkan-loader-devel",
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
    "python-gobject",
    "xwayland-run",
]
pkgdesc = "Gimp Toolkit version 4"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gtk.org"
source = f"$(GNOME_SITE)/gtk/{pkgver[:-2]}/gtk-{pkgver}.tar.xz"
sha256 = "443518b97e8348f9f6430ac435b1010f9a6c5207f4dc6a7cd5d24e3820cee633"
# FIXME overflow in gtklabel.c (repro: gnome-text-editor file reload)
hardening = ["!int"]
# FIXME
options = ["!cross", "!check"]


def post_install(self):
    # we don't really need it (provided by gtk3)
    self.rm(self.destdir / "usr/bin/gtk4-update-icon-cache")
    self.rm(self.destdir / "usr/share/man/man1/gtk4-update-icon-cache.1")


@subpackage("gtk4-devel")
def _devel(self):
    self.depends += ["vulkan-headers"]

    return self.default_devel(
        extra=[
            "usr/bin/gtk4-builder-tool",
            "usr/share/man/man1/gtk4-builder-tool.1",
            "usr/bin/gtk4-encode-symbolic-svg",
            "usr/share/man/man1/gtk4-encode-symbolic-svg.1",
            "usr/bin/gtk4-query-settings",
            "usr/share/man/man1/gtk4-query-settings.1",
            "usr/share/gtk-4.0/valgrind",
        ]
    )


@subpackage("gtk4-demo")
def _demo(self):
    self.pkgdesc = f"{pkgdesc} (demo applications)"

    return [
        "usr/bin/gtk4-demo",
        "usr/bin/gtk4-widget-factory",
        "usr/bin/gtk4-demo-application",
        "usr/bin/gtk4-print-editor",
        "usr/bin/gtk4-node-editor",
        "usr/share/man/man1/gtk4-demo.1",
        "usr/share/man/man1/gtk4-widget-factory.1",
        "usr/share/man/man1/gtk4-demo-application.1",
        "usr/share/man/man1/gtk4-node-editor.1",
        "usr/share/metainfo/org.gtk.Demo4.appdata.xml",
        "usr/share/metainfo/org.gtk.WidgetFactory4.appdata.xml",
        "usr/share/metainfo/org.gtk.gtk4.NodeEditor.appdata.xml",
        "usr/share/gtk-4.0/gtk4builder.rng",
        "usr/share/glib-2.0/schemas/org.gtk.Demo4.gschema.xml",
        "usr/share/applications/org.gtk.Demo4.desktop",
        "usr/share/applications/org.gtk.PrintEditor4.desktop",
        "usr/share/applications/org.gtk.WidgetFactory4.desktop",
        "usr/share/applications/org.gtk.gtk4.NodeEditor.desktop",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.Demo4.svg",
        "usr/share/icons/hicolor/symbolic/apps/org.gtk.Demo4-symbolic.svg",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.PrintEditor4.svg",
        "usr/share/icons/hicolor/symbolic/apps/org.gtk.PrintEditor4-symbolic.svg",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.PrintEditor4.Devel.svg",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.WidgetFactory4.svg",
        "usr/share/icons/hicolor/symbolic/apps/org.gtk.WidgetFactory4-symbolic.svg",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.gtk4.NodeEditor.Devel.svg",
        "usr/share/icons/hicolor/scalable/apps/org.gtk.gtk4.NodeEditor.svg",
        "usr/share/icons/hicolor/symbolic/apps/org.gtk.gtk4.NodeEditor-symbolic.svg",
    ]


@subpackage("gtk4-cups")
def _cups(self):
    self.pkgdesc = f"{pkgdesc} (CUPS print backend)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "cups"]

    return ["usr/lib/gtk-4.0/4.0.0/printbackends/libprintbackend-cups.so"]
