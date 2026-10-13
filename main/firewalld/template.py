pkgname = "firewalld"
pkgver = "2.5.2"
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
    "dinit-dbus",
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
sha256 = "99d7468c22f6cafd8c72aa53173a632f2ca29cb19aec913e8ed45b6102af322d"
# tests don't work in our build env
options = ["etcfiles", "!check"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib")
    self.install_service(self.files_path / "firewalld")


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
        "usr/share/glib-2.0",
        "usr/share/icons/hicolor/*/apps/firewall-config.*",
        "usr/share/man/man1/firewall-config.1",
        "usr/share/metainfo",
    ]


@subpackage("firewalld-firewall-applet")
def _(self):
    self.pkgdesc = "systray applet"
    self.depends = [
        self.parent,
        self.with_pkgver("firewalld-firewall-config"),
        "libnotify",
        "python-pyqt6",
    ]
    self.options = ["etcfiles"]
    return [
        "usr/bin/firewall-applet",
        "usr/share/icons/hicolor/*/apps/firewall-applet*.*",
        "usr/share/man/man1/firewall-applet.1",
        "etc/firewall/applet.conf",
        "etc/xdg/autostart/firewall-applet.desktop",
    ]
