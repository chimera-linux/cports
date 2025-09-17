pkgname = "dbus"
pkgver = "1.16.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dasserts=false",
    "-Ddbus_user=dbus",
    "-Ddoxygen_docs=disabled",
    "-Depoll=enabled",
    "-Dinotify=enabled",
    "-Dselinux=disabled",
    "-Dsystem_pid_file=/run/dbus/pid",
    "-Dsystem_socket=/run/dbus/system_bus_socket",
    "-Dsystemd=disabled",
    "-Duser_session=false",
    "-Dtraditional_activation=true",
    "-Dxml_docs=enabled",
]
hostmakedepends = ["gperf", "meson", "pkgconf", "xmlto"]
makedepends = [
    "dinit-chimera",
    "libexpat-devel",
    "libx11-devel",
    "libcap-devel",
]
triggers = ["/usr/share/dbus-1/system.d"]
pkgdesc = "Message bus system"
license = "GPL-2.0-or-later"
url = "https://dbus.freedesktop.org"
source = f"https://dbus.freedesktop.org/releases/dbus/dbus-{pkgver}.tar.xz"
sha256 = "0ba2a1a4b16afe7bceb2c07e9ce99a8c2c3508e5dec290dbb643384bd6beb7e2"
file_modes = {"usr/lib/dbus-daemon-launch-helper": ("root", "root", 0o4755)}
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
