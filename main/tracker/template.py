pkgname = "tracker"
pkgver = "3.7.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddocs=false",
    "-Dman=true",
    "-Dsystemd_user_services=false",
    "-Dstemmer=disabled",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "asciidoc",
    "xsltproc",
    "dbus",
    "gobject-introspection",
    "python-gobject",
]
makedepends = [
    "glib-devel",
    "dbus-devel",
    "icu-devel",
    "json-glib-devel",
    "libxml2-devel",
    "sqlite-devel",
    "libsoup-devel",
    "bash-completion",
]
depends = ["shared-mime-info"]
pkgdesc = "Search engine and triplestore for desktop, embedded and mobile"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tracker"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "debcaa291e46afadc1cf6a251f17efb02440aa48bff643d78c61123807dce00f"
options = ["!cross"]


@subpackage("tracker-devel")
def _devel(self):
    return self.default_devel()


@subpackage("tracker-libs")
def _libs(self):
    return self.default_libs()
