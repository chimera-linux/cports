# TODO: improve services
pkgname = "deluge"
pkgver = "2.1.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = [
    "python-setuptools", "python-wheel", "intltool"
]
depends = [
    "python-setuptools", "python-chardet", "python-mako", "python-openssl",
    "python-pillow", "python-pyasn1", "python-pyxdg", "python-rencode",
    "python-setproctitle", "python-six", "python-twisted",
    "python-zope.interface", "libtorrent-rasterbar-python",
]
pkgdesc = "Portable BitTorrent client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://deluge-torrent.org"
source = f"https://ftp.osuosl.org/pub/{pkgname}/source/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "768dd319802e42437ab3794ebe75b497142e08ed5b0fb2503bad62cef442dff7"
file_modes = {
    "var/lib/deluge": ("_deluge", "_deluge", 0o755),
    "var/lib/deluge/.config": ("_deluge", "_deluge", 0o755),
    "var/lib/deluge/.config/deluge": ("_deluge", "_deluge", 0o755),
}
# unpackaged checkdepends
options = ["!check"]

system_users = [
    {
        "name": "_deluge",
        "id": None,
        "home": "/var/lib/deluge"
    }
]

def post_install(self):
    # homedir structure, pin it in place
    self.install_dir("var/lib/deluge/.config/deluge", empty = True)
    # default services
    self.install_service(self.files_path / "deluged")
    self.install_service(self.files_path / "deluge-web")

@subpackage("deluge-gtk")
def _gtk(self):
    self.pkgdesc = f"{pkgdesc} (Gtk+3 frontend)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "python-gobject", "gtk+3"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "gtk+3"]

    return [
        "usr/bin/deluge",
        "usr/bin/deluge-gtk",
        "usr/lib/python3*/site-packages/deluge/ui/gtk3",
        "usr/share/appdata",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/man/man1/deluge.1",
        "usr/share/man/man1/deluge-gtk.1",
    ]

@subpackage("deluge-web")
def _web(self):
    self.pkgdesc = f"{pkgdesc} (Web frontend)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "etc/dinit.d/deluge-web",
        "usr/bin/deluge-web",
        "usr/lib/python3*/site-packages/deluge/ui/web",
        "usr/share/man/man1/deluge-web.1",
    ]
