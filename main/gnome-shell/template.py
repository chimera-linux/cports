pkgname = "gnome-shell"
pkgver = "49.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
    "libxslt-progs",
    "meson",
    "perl",
    "pkgconf",
    "python-docutils",
    "sassc",
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
    "ibus",
    "upower",
]
checkdepends = ["xwayland-run"]
pkgdesc = "Core user interface for GNOME"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell"
source = f"$(GNOME_SITE)/gnome-shell/{pkgver.split('.')[0]}/gnome-shell-{pkgver}.tar.xz"
sha256 = "ff086b9c3218099430d9185243b6776a36a2cb7bcb705a98c612f2cf4742708a"
# tests need libmutter-test
options = ["!check", "!cross"]
