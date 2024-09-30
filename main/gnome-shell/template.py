pkgname = "gnome-shell"
pkgver = "47.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dsystemd=false",
    "-Dtests=false",
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "asciidoc",
    "gettext",
    "gjs-devel",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "perl",
    "pkgconf",
    "python-docutils",
    "sassc",
    "xsltproc",
]
makedepends = [
    "at-spi2-core-devel",
    "evolution-data-server-devel",
    "gcr-devel",
    "gjs-devel",
    "gnome-autoar-devel",
    "gnome-bluetooth-devel",
    "gnome-control-center-devel",
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "gstreamer-devel",
    "gtk4-devel",
    "ibus-devel",
    "libpulse-devel",
    "libxml2-devel",
    "mutter-devel",
    "networkmanager-devel",
    "pipewire-devel",
    "polkit-devel",
    "startup-notification-devel",
]
depends = [
    "cmd:unzip!unzip",
    "gnome-control-center",
    "gsettings-desktop-schemas",
    "upower",
]
checkdepends = ["xwayland-run"]
pkgdesc = "Core user interface for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell"
source = f"$(GNOME_SITE)/gnome-shell/{pkgver.split('.')[0]}/gnome-shell-{pkgver}.tar.xz"
sha256 = "7a20770c6290ad69a9a82c8497cb27e1bf863f387db25e98e542e4f6c5f06ded"
patch_style = "patch"
# tests need libmutter-test
options = ["!check", "!cross"]
