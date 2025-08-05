pkgname = "gnome-shell"
pkgver = "48.4"
pkgrel = 0
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
    "upower",
]
checkdepends = ["xwayland-run"]
pkgdesc = "Core user interface for GNOME"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell"
source = f"$(GNOME_SITE)/gnome-shell/{pkgver.split('.')[0]}/gnome-shell-{pkgver}.tar.xz"
sha256 = "40e2ed74b45367f0ca38fbfaa0ab470868d23591d03dc40d0abd6ff77d23b707"
# tests need libmutter-test
options = ["!check", "!cross"]
