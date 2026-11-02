pkgname = "gnome-system-monitor"
pkgver = "51.1"
pkgrel = 0
build_style = "meson"
configure_args = [
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
sha256 = "acf0a61b02b18d20e29cc36cd275ed48fe5e2beeaac99140b299e659cb6493c6"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
