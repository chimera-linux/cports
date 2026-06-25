pkgname = "gmobile"
pkgver = "0.6.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gobject-introspection-devel",
    "json-glib-devel",
]
pkgdesc = "Functions useful in mobile related, glib based projects"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Phosh/gmobile"
source = f"https://sources.phosh.mobi/releases/gmobile/gmobile-{pkgver}.tar.xz"
sha256 = "0786ffd2b0423cd1e5e4998ae4d602fc1f9dbad35c4312b570e0756bfa24cde3"


@subpackage("gmobile-devel")
def _(self):
    return self.default_devel()
