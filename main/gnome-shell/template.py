pkgname = "gnome-shell"
pkgver = "44.3"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
    "-Dtests=false",
    "-Ddefault_library=shared",
    "-Dsoup2=false",
]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext",
    "gobject-introspection",
    "xsltproc",
    "asciidoc",
    "sassc",
    "gjs-devel",
    "glib-devel",
    "perl",
]
makedepends = [
    "gnome-control-center-devel",
    "evolution-data-server-devel",
    "gsettings-desktop-schemas-devel",
    "startup-notification-devel",
    "mutter-devel",
    "at-spi2-core-devel",
    "mutter-devel",
    "gjs-devel",
    "gcr-devel",
    "gtk4-devel",
    "libxml2-devel",
    "ibus-devel",
    "gnome-bluetooth-devel",
    "gstreamer-devel",
    "pipewire-devel",
    "libpulse-devel",
    "gnome-desktop-devel",
    "polkit-devel",
    "networkmanager-devel",
    "gnome-autoar-devel",
]
depends = [
    "gnome-control-center",
    "gsettings-desktop-schemas",
    "upower",
    "cmd:unzip!unzip",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "Core user interface for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "55694b71c2ee4eaef60d93428003f2eaa4cf00186848f5e36b45cfe506fc31bf"
# tests need libmutter-test
options = ["!check"]
