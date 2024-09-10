pkgname = "firewalld"
pkgver = "2.2.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-systemd"]
configure_gen = ["./autogen.sh"]
# icons won't install unless we do this...
make_dir = "."
hostmakedepends = [
    "automake",
    "gtk-doc-tools",
    "intltool",
    "libxml2-progs",
    "pkgconf",
    "python",
]
makedepends = [
    "gettext-devel",
    "glib-devel",
]
depends = [
    "python-dbus",
    "python-gobject",
    "python-nftables",
]
pkgdesc = "Stateful zone-based firewall daemon with D-Bus interface"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://firewalld.org"
source = f"https://github.com/firewalld/firewalld/releases/download/v{pkgver}/firewalld-{pkgver}.tar.bz2"
sha256 = "5215ba30236ee1e3df2c2292465a9ff605b9c445dcab2e37da4961cb27c7f36e"
# tests don't work in our build env
options = ["!check"]


def prepare(self):
    self.rm("src/icons/*/*/firewall-applet*", recursive=True, glob=True)


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib")
    self.install_service(self.files_path / "firewalld")


@subpackage("firewall-config")
def _(self):
    self.pkgdesc = "GTK-based configuration utility for firewalld"
    self.depends = [self.parent, "gtk+3"]
    return [
        "cmd:firewall-config",
        "usr/share/applications",
        "usr/share/firewalld/gtk3_chooserbutton.py",
        "usr/share/firewalld/gtk3_niceexpander.py",
        "usr/share/icons",
        "usr/share/metainfo",
    ]
