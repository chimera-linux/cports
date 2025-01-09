pkgname = "gnome-system-monitor"
pkgver = "47.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
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
sha256 = "ede7b925eb714d8b3c2bfbf7405a1b714494fe47e02f0af08f5837b3e256547f"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
