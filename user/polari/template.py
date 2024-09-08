pkgname = "polari"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
configure_args = ["--libdir=lib"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gtk-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "gjs-devel",
    "glib-devel",
    "gobject-introspection",
    "telepathy-glib-devel",
    "tracker-devel",
]
depends = ["telepathy-idle", "telepathy-mission-control"]
pkgdesc = "GNOME IRC Client"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-2.0-or-later"
url = "https://apps.gnome.org/Polari"
source = f"$(GNOME_SITE)/polari/{pkgver[:-2]}/polari-{pkgver}.tar.xz"
sha256 = "d2b1709e379189294f53d4ef15f03f8bcbbbe8c52f0f415e62f7d5f00c360a31"
