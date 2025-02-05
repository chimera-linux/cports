pkgname = "gnome-system-monitor"
pkgver = "47.1"
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
checkdepends = ["appstream", "desktop-file-utils"]
pkgdesc = "GNOME system monitor"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/SystemMonitor"
source = f"$(GNOME_SITE)/gnome-system-monitor/{pkgver[0 : pkgver.find('.')]}/gnome-system-monitor-{pkgver}.tar.xz"
sha256 = "d3c5714fd91fa7f05d6775e6797ccdab3149f131d1aa776a3352e2addb110f01"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
