pkgname = "gnome-system-monitor"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "itstool",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "glibmm-devel",
    "gtkmm-devel",
    "libadwaita-devel",
    "libgtop-devel",
    "librsvg-devel",
    "libxml2-devel",
    "libxslt-devel",
    "polkit-devel",
]
checkdepends = ["appstream-glib-devel", "desktop-file-utils"]
pkgdesc = "GNOME system monitor"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/SystemMonitor"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[0:pkgver.find('.')]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5376248158c686c308255472e8c2a9e4c17255642c149fc7198c6d034e547599"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
