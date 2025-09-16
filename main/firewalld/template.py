pkgname = "firewalld"
pkgver = "2.3.1"
pkgrel = 0
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
    "dinit-chimera",
    "gettext-devel",
    "glib-devel",
]
depends = [
    "dinit-dbus",
    "python-dbus",
    "python-gobject",
    "python-nftables",
]
pkgdesc = "Stateful zone-based firewall daemon with D-Bus interface"
license = "GPL-2.0-or-later"
url = "https://firewalld.org"
source = f"https://github.com/firewalld/firewalld/releases/download/v{pkgver}/firewalld-{pkgver}.tar.bz2"
sha256 = "719890d82caa7d162b021ed646034883b9eb354a45de3685c28ead057d139d4d"
# tests don't work in our build env
options = ["!check"]


def prepare(self):
    self.rm("src/icons/*/*/firewall-applet*", recursive=True, glob=True)


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib")
    self.install_service("^/firewalld")


@subpackage("firewalld-firewall-config")
def _(self):
    self.pkgdesc = "GTK-based configuration utility for firewalld"
    self.depends = [self.parent, "gtk+3"]
    self.renames = ["firewall-config"]
    return [
        "usr/bin/firewall-config",
        "usr/share/applications",
        "usr/share/firewalld/gtk3_chooserbutton.py",
        "usr/share/firewalld/gtk3_niceexpander.py",
        "usr/share/icons",
        "usr/share/man/man1/firewall-config.1",
        "usr/share/metainfo",
    ]
