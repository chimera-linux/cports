pkgname = "dbus"
pkgver = "1.14.10"
pkgrel = 14
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "--disable-selinux",
    "--disable-asserts",
    "--disable-systemd",
    "--disable-user-session",
    "--disable-doxygen-docs",
    "--enable-inotify",
    "--enable-xml-docs",
    "--enable-epoll",
    "--enable-traditional-activation",
    "--with-dbus-user=dbus",
    "--with-system-socket=/run/dbus/system_bus_socket",
    "--with-system-pid-file=/run/dbus/pid",
]
configure_gen = []
hostmakedepends = ["gperf", "pkgconf", "xmlto"]
makedepends = ["libexpat-devel", "libx11-devel", "libcap-devel"]
triggers = ["/usr/share/dbus-1/system.d"]
scripts = {"pre-install": True, "pre-upgrade": True}
pkgdesc = "Message bus system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://dbus.freedesktop.org"
source = f"https://dbus.freedesktop.org/releases/dbus/dbus-{pkgver}.tar.xz"
sha256 = "ba1f21d2bd9d339da2d4aa8780c09df32fea87998b73da24f49ab9df1e36a50f"
file_modes = {"usr/lib/dbus-daemon-launch-helper": ("root", "dbus", 0o4750)}
hardening = ["vis", "!cfi"]
options = ["linkundefver"]


def post_install(self):
    # service file
    self.install_file(
        self.files_path / "dbus-session.wrapper", "usr/lib", mode=0o755
    )
    self.install_service(self.files_path / "dbus-daemon", enable=True)
    self.install_service(self.files_path / "dbus-daemon.user", enable=True)
    # x11 support
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "01dbus-env", "etc/X11/Xsession.d", mode=0o755
    )
    # sysuser and tmpfiles
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("dbus-devel")
def _(self):
    self.depends += ["libexpat-devel"]
    return self.default_devel(
        extra=[
            "usr/lib/dbus-1.0",
            "usr/share/doc",
        ]
    )


@subpackage("dbus-libs")
def _(self):
    return self.default_libs()


@subpackage("dbus-x11")
def _(self):
    self.subdesc = "X11 support"
    self.depends = [self.parent]
    self.install_if = [self.parent, "xinit"]
    return [
        "etc/X11/Xsession.d",
        "usr/bin/dbus-launch",
        "usr/share/man/man1/dbus-launch.1",
    ]
