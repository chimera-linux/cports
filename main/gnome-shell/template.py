pkgname = "gnome-shell"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false", "-Dtests=false", "-Ddefault_library=shared",
    "-Dsoup2=false",
]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "gobject-introspection",
    "xsltproc", "asciidoc", "sassc", "gjs-devel", "glib-devel", "perl",
]
makedepends = [
    "gnome-control-center-devel", "evolution-data-server-devel",
    "gsettings-desktop-schemas-devel", "startup-notification-devel",
    "mutter-devel", "at-spi2-core-devel", "mutter-devel", "gjs-devel",
    "gcr4-devel", "gtk4-devel", "libxml2-devel", "ibus-devel",
    "gnome-bluetooth-devel", "gstreamer-devel", "pipewire-devel",
    "libpulse-devel", "gnome-desktop-devel", "polkit-devel",
    "networkmanager-devel", "gnome-autoar-devel",
]
depends = [
    "gnome-control-center", "gsettings-desktop-schemas", "upower"
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "Core user interface for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3310adc1dd4e210998d59f3871bc31f7e04915428d9ced88c2a66b2b05d6c00a"
# tests need libmutter-test
options = ["!check"]
