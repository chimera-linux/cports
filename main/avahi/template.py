# this must be synchronized with avahi-ui-progs
pkgname = "avahi"
pkgver = "0.8"
pkgrel = 9
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
    "--disable-static",
    "--disable-introspection",
    "--enable-compat-libdns_sd",
    "--enable-compat-howl",
    "--enable-python",
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
depends = ["dinit-dbus"]
pkgdesc = "Multicast DNS Service Discovery"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lathiat/avahi"
source = f"{url}/releases/download/v{pkgver}/avahi-{pkgver}.tar.gz"
sha256 = "060309d7a333d38d951bc27598c677af1796934dbd98e1024e7ad8de798fedda"
options = ["!cross"]


def post_install(self):
    # is in avahi-python
    self.uninstall("usr/lib/python*", glob=True)
    self.uninstall("usr/share/man/man1/avahi-bookmarks.1")
    # service
    self.install_service(self.files_path / "avahi-daemon")
    self.install_sysusers(self.files_path / "sysusers.conf")


@subpackage("avahi-autoipd")
def _(self):
    self.pkgdesc = "Avahi IPv4LL network address configuration daemon"

    return [
        "etc/avahi/avahi-autoipd.action",
        "cmd:avahi-autoipd",
        "man:avahi-autoipd*.8",
    ]


@subpackage("avahi-compat-devel")
def _(self):
    self.depends += [self.with_pkgver("avahi-devel")]
    self.subdesc = "compat development files"

    return [
        "usr/include/avahi-compat*",
        "usr/lib/pkgconfig/avahi-compat*",
        "usr/lib/libhowl.so",
        "usr/lib/libdns_sd.so",
    ]


@subpackage("avahi-compat-libs")
def _(self):
    self.subdesc = "compat libraries"

    return [
        "usr/lib/libhowl.so.*",
        "usr/lib/libdns_sd.so.*",
    ]


@subpackage("avahi-devel")
def _(self):
    self.depends += ["dbus-devel"]

    return self.default_devel()


@subpackage("avahi-libs")
def _(self):
    return self.default_libs()


@subpackage("avahi-progs")
def _(self):
    # do not take daemon
    return [
        "cmd:avahi-browse*",
        "cmd:avahi-publish*",
        "cmd:avahi-resolve*",
    ]
