pkgname = "gnome-shell"
pkgver = "41.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false", "-Dtests=false", "-Ddefault_library=shared"
]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "gobject-introspection",
    "xsltproc", "asciidoc", "sassc", "gjs-devel", "glib-devel", "perl",
]
makedepends = [
    "gnome-control-center-devel", "evolution-data-server-devel",
    "gsettings-desktop-schemas-devel", "startup-notification-devel",
    "mutter-devel", "at-spi2-atk-devel", "mutter-devel", "gjs-devel",
    "gcr-devel", "gtk+3-devel", "libxml2-devel", "ibus-devel",
    "gnome-bluetooth-devel", "gstreamer-devel", "pipewire-devel",
    "libpulse-devel", "gnome-desktop-devel", "elogind-devel",
    "polkit-devel", "networkmanager-devel", "gnome-autoar-devel",
    "gtk4-devel",
]
depends = [
    "elogind", "gnome-control-center", "gsettings-desktop-schemas", "upower"
]
pkgdesc = "Core user interface for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1e3dfa2a0be49454182b4ace77f11d10d3f5b988ef0fcb732b7313573949ded1"
# would need xvfb-run
options = ["!check"]
