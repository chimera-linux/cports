# TODO: improve services
pkgname = "deluge"
pkgver = "2.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "intltool",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["dinit-chimera"]
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
license = "GPL-3.0-or-later"
url = "https://deluge-torrent.org"
source = f"https://ftp.osuosl.org/pub/deluge/source/{pkgver[:-2]}/deluge-{pkgver}.tar.xz"
sha256 = "b9ba272b5ba42aaf1c694e6c29628ab816cc1a700a37bac08aacb52571606acd"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        "deluge/ui/data/share/metainfo/deluge.metainfo.xml",
        "usr/share/metainfo",
    )
    self.install_file(
        "deluge/ui/data/share/applications/deluge.desktop",
        "usr/share/applications",
    )
    # default services
    self.install_service(self.files_path / "deluged")
    self.install_service(self.files_path / "deluge-web")


@subpackage("deluge-gtk")
def _(self):
    self.subdesc = "Gtk+3 frontend"
    self.depends = [self.parent, "python-gobject", "gtk+3"]
    self.install_if = [self.parent, "gtk+3"]
    # FIXME lintpixmaps
    self.options = ["!lintpixmaps"]

    return [
        "usr/bin/deluge",
        "usr/bin/deluge-gtk",
        "usr/lib/python3*/site-packages/deluge/ui/gtk3",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/metainfo",
        "usr/share/pixmaps",
        "usr/share/man/man1/deluge.1",
        "usr/share/man/man1/deluge-gtk.1",
    ]


@subpackage("deluge-web")
def _(self):
    self.subdesc = "Web frontend"
    self.depends = [self.parent]

    return [
        "usr/bin/deluge-web",
        "usr/lib/dinit.d/deluge-web",
        "usr/lib/python3*/site-packages/deluge/ui/web",
        "usr/share/man/man1/deluge-web.1",
    ]
