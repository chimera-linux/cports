pkgname = "cdrdao"
pkgver = "1.2.6"
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
license = "GPL-2.0-or-later"
url = "https://github.com/cdrdao/cdrdao"
source = f"{url}/archive/refs/tags/rel_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "ba3eadcae7b62a709e9e23988d7fb41f822c408dcec9bd99ff1a343d1bcbc524"


def post_install(self):
    # literally only thing installing anything here
    self.uninstall("usr/share/mime-info")
    # fix the pixmap location too while at it
    self.uninstall("usr/share/pixmaps")
    # less scuffed icon lol (the other is 48x48)
    self.install_file(
        "gcdmaster/gcdmaster-doc.png",
        "usr/share/icons/hicolor/96x96/apps",
        name="gcdmaster.png",
    )


@subpackage("cdrdao-gcdmaster")
def _(self):
    self.subdesc = "GTK interface"
    self.depends = [self.parent]

    return [
        "cmd:gcdmaster",
        "usr/share/application*",
        "usr/share/gcdmaster",
        "usr/share/glib-2.0",
        "usr/share/icons",
        "usr/share/mime*",
    ]
