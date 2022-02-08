pkgname = "dbus"
pkgver = "1.12.20"
pkgrel = 0
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
    "--enable-elogind",
    "--with-dbus-user=dbus",
    "--with-system-socket=/run/dbus/system_bus_socket",
    "--with-system-pid-file=/run/dbus/pid",
    "--with-console-auth-dir=/run/console",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "gperf", "pkgconf", "xmlto"]
makedepends = [
    "elogind-devel", "libexpat-devel", "libx11-devel", "libcap-devel"
]
install_if = ["elogind", f"dbus-libs={pkgver}-r{pkgrel}"]
pkgdesc = "Message bus system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://dbus.freedesktop.org"
source = f"https://dbus.freedesktop.org/releases/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "f77620140ecb4cdc67f37fb444f8a6bea70b5b6461f12f1cbe2cec60fa7de5fe"
suid_files = [
    "usr/libexec/dbus-daemon-launch-helper"
]
file_modes = {
    "usr/libexec/dbus-daemon-launch-helper": (None, "dbus:22", 0o4750)
}

system_users = ["dbus:22"]

def post_install(self):
    # these need to exist
    self.install_dir("var/lib/dbus", empty = True)
    self.install_dir("etc/dbus-1/session.d", empty = True)
    # service file
    self.install_file(
        self.files_path / "dbus-daemon.wrapper", "usr/libexec", mode = 0o755
    )
    self.install_file(
        self.files_path / "dbus-session.wrapper", "usr/libexec", mode = 0o755
    )
    self.install_service(self.files_path / "dbus-prepare")
    self.install_service(self.files_path / "dbus")
    self.install_service(self.files_path / "dbus.user")

@subpackage("dbus-devel")
def _devel(self):
    self.depends += ["libexpat-devel"]
    return self.default_devel(extra = [
        "usr/lib/dbus-*",
        "usr/share/doc",
    ])

@subpackage("dbus-libs")
def _libs(self):
    return self.default_libs()

@subpackage("dbus-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "xserver-xorg-core"]
    return [
        "usr/bin/dbus-launch",
        "usr/share/man/man1/dbus-launch.1",
    ]
