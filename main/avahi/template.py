pkgname = "avahi"
pkgver = "0.8"
pkgrel = 10
build_style = "gnu_configure"
configure_args = [
    "--disable-qt3",
    "--disable-qt4",
    "--disable-qt5",
    "--disable-gtk",
    "--disable-dbm",
    "--disable-gdbm",
    "--disable-mono",
    "--disable-monodoc",
    "--disable-doxygen-doc",
    "--disable-static",
    "--enable-gtk3",
    "--enable-glib",
    "--enable-gobject",
    "--enable-pygobject",
    "--enable-introspection",
    "--enable-compat-libdns_sd",
    "--enable-compat-howl",
    "--enable-python",
    "--enable-xmltoman",
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
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "libtool",
    "pkgconf",
    "python",
    "python-dbus",
    "xmltoman",
]
makedepends = [
    "dbus-devel",
    "gtk+3-devel",
    "libcap-devel",
    "libdaemon-devel",
    "libevent-devel",
    "python-gobject-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Multicast DNS Service Discovery"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lathiat/avahi"
source = f"{url}/releases/download/v{pkgver}/avahi-{pkgver}.tar.gz"
sha256 = "060309d7a333d38d951bc27598c677af1796934dbd98e1024e7ad8de798fedda"
options = ["!cross"]


def post_install(self):
    self.install_service(self.files_path / "avahi-daemon")
    self.install_sysusers(self.files_path / "sysusers.conf")


@subpackage("avahi-python")
def _(self):
    self.pkgdesc = "Python utility package for Avahi"
    self.depends = ["python", "python-dbus"]

    return [
        "usr/bin/avahi-bookmarks",
        "usr/lib/python3*",
        "usr/share/man/man1/avahi-bookmarks*",
    ]


@subpackage("avahi-glib-devel")
def _(self):
    self.pkgdesc = "Avahi glib libraries"
    self.depends = [f"avahi-devel~{pkgver}"]

    return [
        "usr/include/avahi-g*",
        "usr/lib/libavahi-glib.so",
        "usr/lib/libavahi-gobject.so",
        "usr/lib/pkgconfig/avahi-g*",
        "usr/share/gir-1.0",
    ]


@subpackage("avahi-glib-libs")
def _(self):
    self.pkgdesc = "Avahi glib libraries"

    return [
        "usr/lib/libavahi-glib.so.*",
        "usr/lib/libavahi-gobject.so.*",
        "usr/lib/girepository-1.0",
    ]


@subpackage("avahi-ui-progs")
def _(self):
    self.pkgdesc = "Avahi Gtk+ utilities"
    self.depends = [self.parent]

    return [
        "cmd:avahi-discover-standalone",
        "cmd:bshell",
        "cmd:bssh",
        "cmd:bvnc",
        "usr/share/applications/bssh.desktop",
        "usr/share/applications/bvnc.desktop",
        "usr/share/avahi/interfaces/avahi-discover.ui",
    ]


@subpackage("avahi-ui-devel")
def _(self):
    self.pkgdesc = "Avahi UI libraries"
    self.depends = [f"avahi-devel~{pkgver}"]

    return [
        "usr/include/avahi-ui",
        "usr/lib/libavahi-ui*.so",
        "usr/lib/pkgconfig/avahi-ui*",
    ]


@subpackage("avahi-ui-libs")
def _(self):
    self.pkgdesc = "Avahi UI libraries"

    return [
        "usr/lib/libavahi-ui*.so.*",
    ]


@subpackage("avahi-libevent-devel")
def _(self):
    self.pkgdesc = "Avahi libevent libraries"
    self.depends = [f"avahi-devel~{pkgver}"]

    return [
        "usr/include/avahi-libevent*",
        "usr/lib/libavahi-libevent*.so",
        "usr/lib/pkgconfig/avahi-libevent*",
    ]


@subpackage("avahi-libevent-libs")
def _(self):
    self.pkgdesc = "Avahi libevent libraries"

    return [
        "usr/lib/libavahi-libevent*.so.*",
    ]


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
