pkgname = "gnome-system-monitor"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dsystemd=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "glibmm-devel",
    "gtkmm-devel",
    "libadwaita-devel",
    "libgtop-devel",
    "librsvg-devel",
    "libxml2-devel",
]
checkdepends = ["appstream", "catch2-devel", "desktop-file-utils"]
pkgdesc = "GNOME system monitor"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/SystemMonitor"
source = f"$(GNOME_SITE)/gnome-system-monitor/{pkgver[0 : pkgver.find('.')]}/gnome-system-monitor-{pkgver}.tar.xz"
sha256 = "e4e5b345fbd4d7dc2f40ad6c62305ae5c7cc2b465ce95988692a54af347532a3"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
