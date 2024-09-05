pkgname = "gnome-system-monitor"
pkgver = "47_rc"
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
source = f"$(GNOME_SITE)/gnome-system-monitor/{pkgver[:2]}/gnome-system-monitor-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "fd01dc2b1b674ccbf3d9a17b5c1a299562824922139803e903c5db8a73ee7855"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
