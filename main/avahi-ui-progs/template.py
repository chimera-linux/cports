# this must be synchronized with avahi; it exists to avoid build-time cycles
pkgname = "avahi-ui-progs"
pkgver = "0.8"
pkgrel = 1
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
    "--with-distro=none",
    "--with-dbus-system-socket=unix:path=/run/dbus/system_bus_socket",
    "--without-systemdsystemunitdir",
    "ssp_cv_lib=no",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gmake",
    "gobject-introspection",
    "libtool",
    "pkgconf",
    "python",
    "python-dbus",
    "xmltoman",
]
makedepends = [
    "avahi-devel",
    "dbus-devel",
    "gtk+3-devel",
    "libcap-devel",
    "libdaemon-devel",
    "libevent-devel",
    "python-gobject-devel",
]
depends = [f"avahi~{pkgver}"]
pkgdesc = "Avahi Gtk+ utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lathiat/avahi"
source = f"{url}/releases/download/v{pkgver}/avahi-{pkgver}.tar.gz"
sha256 = "060309d7a333d38d951bc27598c677af1796934dbd98e1024e7ad8de798fedda"
options = ["!cross"]


def do_install(self):
    if (self.cwd / "tinst").is_dir():
        self.rm("tinst", recursive=True)
    self.mkdir("tinst")

    self.make.install(
        ["DESTDIR=" + str(self.chroot_cwd / "tinst")], default_args=False
    )

    self.install_dir("usr/bin")
    self.install_dir("usr/include")
    self.install_dir("usr/lib/pkgconfig")
    self.install_dir("usr/share/applications")
    self.install_dir("usr/share/avahi/interfaces")
    self.install_dir("usr/share/man/man1")

    for f in [
        "bvnc",
        "bssh",
        "bshell",
        "avahi-bookmarks",
        "avahi-discover-standalone",
    ]:
        self.mv(f"tinst/usr/bin/{f}", self.destdir / "usr/bin")
        # manpage if it exists
        if (self.cwd / f"tinst/usr/share/man/man1/{f}.1").exists():
            self.mv(
                f"tinst/usr/share/man/man1/{f}.1",
                self.destdir / "usr/share/man/man1",
            )
        # desktop file if it exists
        if (self.cwd / f"tinst/usr/share/applications/{f}.desktop").exists():
            self.mv(
                f"tinst/usr/share/applications/{f}.desktop",
                self.destdir / "usr/share/applications",
            )

    def _mv(pattern):
        ip = self.cwd / "tinst" / pattern
        td = self.destdir / ip.parent.relative_to(self.cwd / "tinst")
        for f in ip.parent.glob(ip.name):
            self.mv(f, td)

    # all the other stuff
    _mv("usr/include/avahi-g*")
    _mv("usr/include/avahi-ui*")
    _mv("usr/include/avahi-libevent*")
    _mv("usr/lib/python3*")
    _mv("usr/lib/*avahi-g*")
    _mv("usr/lib/*avahi-ui*")
    _mv("usr/lib/*avahi-libevent*")
    _mv("usr/lib/pkgconfig/avahi-g*")
    _mv("usr/lib/pkgconfig/avahi-ui*")
    _mv("usr/lib/pkgconfig/avahi-libevent*")
    _mv("usr/share/avahi/interfaces/*.ui")
    _mv("usr/lib/girepository-1.0")
    _mv("usr/share/gir-1.0")


@subpackage("avahi-python")
def _pyprogs(self):
    self.pkgdesc = "Python utility package for Avahi"
    self.depends = ["python", "python-dbus"]

    return [
        "usr/bin/avahi-bookmarks",
        "usr/lib/python3*",
        "usr/share/man/man1/avahi-bookmarks*",
    ]


@subpackage("avahi-glib-devel")
def _gdevel(self):
    self.pkgdesc = "Avahi glib libraries (development files)"
    self.depends = [f"avahi-devel~{pkgver}"]

    return [
        "usr/include/avahi-g*",
        "usr/lib/libavahi-glib.so",
        "usr/lib/libavahi-gobject.so",
        "usr/lib/pkgconfig/avahi-g*",
        "usr/share/gir-1.0",
    ]


@subpackage("avahi-glib-libs")
def _glibs(self):
    self.pkgdesc = "Avahi glib libraries"

    return [
        "usr/lib/libavahi-glib.so.*",
        "usr/lib/libavahi-gobject.so.*",
        "usr/lib/girepository-1.0",
    ]


@subpackage("avahi-ui-devel")
def _udevel(self):
    self.pkgdesc = "Avahi UI libraries (development files)"
    self.depends = [f"avahi-devel~{pkgver}"]

    return [
        "usr/include/avahi-ui",
        "usr/lib/libavahi-ui*.so",
        "usr/lib/pkgconfig/avahi-ui*",
    ]


@subpackage("avahi-ui-libs")
def _ulibs(self):
    self.pkgdesc = "Avahi UI libraries"

    return [
        "usr/lib/libavahi-ui*.so.*",
    ]


@subpackage("avahi-libevent-devel")
def _edevel(self):
    self.pkgdesc = "Avahi libevent libraries (development files)"
    self.depends = [f"avahi-devel~{pkgver}"]

    return [
        "usr/include/avahi-libevent*",
        "usr/lib/libavahi-libevent*.so",
        "usr/lib/pkgconfig/avahi-libevent*",
    ]


@subpackage("avahi-libevent-libs")
def _elibs(self):
    self.pkgdesc = "Avahi libevent libraries"

    return [
        "usr/lib/libavahi-libevent*.so.*",
    ]
