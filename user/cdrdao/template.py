pkgname = "cdrdao"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-gcdmaster",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "gtkmm3.0-devel",
    "lame-devel",
    "libao-devel",
    "libvorbis-devel",
    "linux-headers",
]
pkgdesc = "Disk-at-once CD writer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/cdrdao/cdrdao"
source = f"{url}/archive/refs/tags/rel_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "b347189ab550ae5bd1a19d323cdfd8928039853c23aa5e33d7273ab8c750692a"


@subpackage("cdrdao-gcdmaster")
def _(self):
    self.subdesc = "(GTK interface)"
    self.depends = [self.parent]
    return [
        "cmd:gcdmaster",
        "usr/share/application*",
        "usr/share/gcdmaster",
        "usr/share/glib-2.0",
        "usr/share/mime*",
        "usr/share/pixmaps",
    ]
