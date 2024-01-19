pkgname = "dbus"
pkgver = "1.14.10"
pkgrel = 8
build_style = "gnu_configure"
configure_args = [
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
make_cmd = "gmake"
hostmakedepends = ["gmake", "gperf", "pkgconf", "xmlto"]
makedepends = ["libexpat-devel", "libx11-devel", "libcap-devel"]
triggers = ["/usr/share/dbus-1/system.d"]
pkgdesc = "Message bus system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://dbus.freedesktop.org"
source = (
    f"https://dbus.freedesktop.org/releases/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "ba1f21d2bd9d339da2d4aa8780c09df32fea87998b73da24f49ab9df1e36a50f"
suid_files = ["usr/libexec/dbus-daemon-launch-helper"]
file_modes = {"usr/libexec/dbus-daemon-launch-helper": ("root", "dbus", 0o4750)}
# FIXME cfi
hardening = ["vis", "!cfi"]
options = ["linkundefver"]

system_users = ["dbus:22"]


def post_install(self):
    # service file
    self.install_file(
        self.files_path / "dbus-session.wrapper", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "dbus", enable=True)
    self.install_service(self.files_path / "dbus.user", enable=True)
    # x11 support
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "01dbus-env", "etc/X11/Xsession.d", mode=0o755
    )
    # sysuser and tmpfiles
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="dbus.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="dbus.conf",
    )


@subpackage("dbus-devel")
def _devel(self):
    self.depends += ["libexpat-devel"]
    return self.default_devel(
        extra=[
            "usr/lib/dbus-*",
            "usr/share/doc",
        ]
    )


@subpackage("dbus-libs")
def _libs(self):
    return self.default_libs()


@subpackage("dbus-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "xinit"]
    return [
        "etc/X11/Xsession.d",
        "usr/bin/dbus-launch",
        "usr/share/man/man1/dbus-launch.1",
    ]
