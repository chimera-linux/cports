pkgname = "gnome-system-monitor"
pkgver = "50.0"
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
sha256 = "a4138aa754b4584c46de91fad1d685e27b12bc2457de761863b6be02d84c4862"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
