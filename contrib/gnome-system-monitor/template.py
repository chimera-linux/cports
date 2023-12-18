pkgname = "gnome-system-monitor"
pkgver = "45.0.2"
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
    "gtkmm3.0-devel",
    "libgtop-devel",
    "libhandy-devel",
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
sha256 = "c5e272d90bf9986a3f8613d76e0d27fa42dfacee5c0192e73921bb94b1868a2e"
tool_flags = {"CFLAGS": ["-D_BSD_SOURCE"]}
