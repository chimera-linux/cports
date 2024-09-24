pkgname = "gtk4"
pkgver = "4.16.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dman-pages=true",
    "-Ddocumentation=false",
    "-Dbroadway-backend=true",
    "-Dx11-backend=true",
    "-Dwayland-backend=true",
    "-Dintrospection=enabled",
    "-Dcolord=enabled",
    "-Dvulkan=enabled",
    "-Dcloudproviders=enabled",
    "-Dtracker=enabled",
    # not installed
    "-Dbuild-examples=false",
    # disabled below
    "-Dbuild-testsuite=false",
    "-Dbuild-tests=false",
]
make_check_args = ["--timeout-multiplier=4"]
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
    "bash",
    "dbus",
    "fonts-cantarell-otf",
    "fonts-dejavu",
    "fonts-noto",
    "librsvg",
    "python-gobject",
    "xwayland-run",
]
pkgdesc = "Gimp Toolkit version 4"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gtk.org"
source = f"$(GNOME_SITE)/gtk/{pkgver[:-2]}/gtk-{pkgver}.tar.xz"
sha256 = "34b624848e5de22a138b675ad6f39c0c7b9d67907c10e1fc7e5b03060e8d5437"
# FIXME: manifests as a crash in gnome-text-editor when
# an externally modified file reloads; happens always
hardening = ["!int"]
# check: most of them crash presently
options = ["!cross", "!check"]


def post_install(self):
    # we don't really need it (provided by gtk3)
    # note: there are no changes in this since gtk3 aside from warning cleanups anyway
    self.uninstall("usr/bin/gtk4-update-icon-cache")
    self.uninstall("usr/share/man/man1/gtk4-update-icon-cache.1")


@subpackage("gtk4-devel")
def _(self):
    self.depends += ["vulkan-headers"]

    return self.default_devel(
        extra=[
            "cmd:gtk4-builder-tool",
            "cmd:gtk4-encode-symbolic-svg",
            "cmd:gtk4-query-settings",
            "usr/share/gtk-4.0/valgrind",
        ]
    )


@subpackage("gtk4-demo")
def _(self):
    self.subdesc = "demo applications"

    return [
        "cmd:gtk4-demo",
        "cmd:gtk4-widget-factory",
        "cmd:gtk4-demo-application",
        "cmd:gtk4-print-editor",
        "cmd:gtk4-node-editor",
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
def _(self):
    self.subdesc = "CUPS print backend"
    self.install_if = [self.parent, "cups"]

    return ["usr/lib/gtk-4.0/4.0.0/printbackends/libprintbackend-cups.so"]
