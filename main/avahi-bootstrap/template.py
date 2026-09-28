pkgname = "avahi-bootstrap"
pkgver = "0.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-qt3",
    "--disable-qt4",
    "--disable-qt5",
    "--disable-gtk",
    "--disable-gtk3",
    "--disable-glib",
    "--disable-gobject",
    "--disable-libevent",
    "--disable-dbm",
    "--disable-gdbm",
    "--disable-mono",
    "--disable-monodoc",
    "--disable-doxygen-doc",
    "--disable-xmltoman",
    "--disable-pygobject",
    "--disable-python-dbus",
    "--disable-python",
    "--disable-static",
    "--disable-introspection",
    "--disable-compat-libdns_sd",
    "--disable-compat-howl",
    "--with-xml=expat",
    "--with-avahi-user=_avahi",
    "--with-avahi-group=_avahi",
    "--with-autoipd-user=_avahi",
    "--with-autoipd-group=_avahi",
    "--with-avahi-priv-access-group=network",
    "--with-dbus-sys=/usr/share/dbus-1/system.d",
    "--with-distro=none",
    "--with-dbus-system-socket=unix:path=/run/dbus/system_bus_socket",
    "--without-systemdsystemunitdir",
    "ssp_cv_lib=no",
]
configure_gen = []
hostmakedepends = ["pkgconf", "python", "gettext"]
makedepends = ["dbus-devel", "libcap-devel", "libdaemon-devel"]
depends = [
    "!avahi",
    "!avahi-compat-devel",
    "!avahi-compat-libs",
    "!avahi-devel",
    "!avahi-libs",
]
provides = [
    "so:libavahi-client.so.3=0",
    "so:libavahi-common.so.3=0",
    "so:libavahi-core.so.7=0",
    "pc:avahi-client=0.7.9",
    "pc:avahi-core=0.7.9",
]
pkgdesc = "Multicast DNS Service Discovery"
subdesc = "bootstrap package"
license = "LGPL-2.1-or-later"
url = "https://github.com/lathiat/avahi"
source = f"{url}/releases/download/v{pkgver}/avahi-{pkgver}.tar.gz"
sha256 = "060309d7a333d38d951bc27598c677af1796934dbd98e1024e7ad8de798fedda"
options = [
    "!cross",
    "!scancmd",
    "!scanpkgconf",
    "!scanshlibs",
    "!autosplit",
]


def post_install(self):
    self.uninstall("etc")
    self.uninstall("usr/share")
