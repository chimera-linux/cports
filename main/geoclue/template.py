pkgname = "geoclue"
pkgver = "2.5.7.99"
pkgrel = 0
# we use a recent commit since it would be a pain to rebase the soup3 patch
_commit = "df071a060190de925628afd0aa2e9ec739bf90d8"
build_style = "meson"
configure_args = [
    "-Ddbus-srv-user=_geoclue",
    "-Dgtk-doc=false",
    "-Dintrospection=true",
    "-Dvapi=true",
    "-Dsoup2=false",
    "-Ddemo-agent=false", # problematic meson.build
    # FIXME: this needs avahi glib libs
    "-Dnmea-source=false",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection", "vala",
]
makedepends = [
    "eudev-devel", "json-glib-devel", "libsoup-devel", "libnotify-devel",
    "modemmanager-devel",
]
pkgdesc = "D-Bus geoinformation service"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/geoclue/geoclue/wikis/home"
source = f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/{_commit}.tar.bz2"
sha256 = "489db5383cf384549e57df257150dc7a69ff76aa0aa4e28b6a0f2ed13a8dd865"

system_users = ["_geoclue"]

@subpackage("geoclue-devel")
def _devel(self):
    return self.default_devel()
