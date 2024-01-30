pkgname = "firewalld"
pkgver = "2.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-systemd"]
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
# icons won't install unless we do this...
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
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
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://firewalld.org"
source = f"https://github.com/firewalld/firewalld/releases/download/v{pkgver}/firewalld-{pkgver}.tar.bz2"
sha256 = "a138a3799b5f6e6539bac308e5ae8950998d5173f588231214e979524e7c9416"
# tests don't work in our build env
options = ["!check"]


def do_prepare(self):
    self.rm("src/icons/*/*/firewall-applet*", recursive=True, glob=True)


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib")
    self.install_service(self.files_path / "firewalld")


@subpackage("firewall-config")
def _config(self):
    self.pkgdesc = "GTK-based configuration utility for firewalld"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "gtk+3"]
    return [
        "usr/bin/firewall-config",
        "usr/share/applications",
        "usr/share/firewalld/gtk3_chooserbutton.py",
        "usr/share/firewalld/gtk3_niceexpander.py",
        "usr/share/icons",
        "usr/share/man/man1/firewall-config.1",
        "usr/share/metainfo",
    ]
