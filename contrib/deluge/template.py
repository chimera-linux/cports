# TODO: improve services
pkgname = "deluge"
pkgver = "2.1.1"
pkgrel = 3
build_style = "python_pep517"
hostmakedepends = [
    "intltool",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "libtorrent-rasterbar-python",
    "python-chardet",
    "python-mako",
    "python-openssl",
    "python-pillow",
    "python-pyasn1",
    "python-pyxdg",
    "python-rencode",
    "python-setproctitle",
    "python-setuptools",
    "python-six",
    "python-twisted",
    "python-zope.interface",
]
pkgdesc = "Portable BitTorrent client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://deluge-torrent.org"
source = f"https://ftp.osuosl.org/pub/deluge/source/{pkgver[:-2]}/deluge-{pkgver}.tar.xz"
sha256 = "768dd319802e42437ab3794ebe75b497142e08ed5b0fb2503bad62cef442dff7"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        "deluge/ui/data/share/appdata/deluge.appdata.xml", "usr/share/appdata"
    )
    self.install_file(
        "deluge/ui/data/share/applications/deluge.desktop",
        "usr/share/applications",
    )
    # default services
    self.install_service(self.files_path / "deluged")
    self.install_service(self.files_path / "deluge-web")


@subpackage("deluge-gtk")
def _gtk(self):
    self.subdesc = "Gtk+3 frontend"
    self.depends = [self.parent, "python-gobject", "gtk+3"]
    self.install_if = [self.parent, "gtk+3"]

    return [
        "usr/bin/deluge",
        "usr/bin/deluge-gtk",
        "usr/lib/python3*/site-packages/deluge/ui/gtk3",
        "usr/share/appdata",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/pixmaps",
        "usr/share/man/man1/deluge.1",
        "usr/share/man/man1/deluge-gtk.1",
    ]


@subpackage("deluge-web")
def _web(self):
    self.subdesc = "Web frontend"
    self.depends = [self.parent]

    return [
        "etc/dinit.d/deluge-web",
        "usr/bin/deluge-web",
        "usr/lib/python3*/site-packages/deluge/ui/web",
        "usr/share/man/man1/deluge-web.1",
    ]
