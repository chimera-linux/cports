pkgname = "dinit-chimera"
pkgver = "0.99.7"
pkgrel = 3
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
depends = [
    "dinit",
    "tzdata",
    "virtual:cmd:awk!chimerautils",
    "virtual:cmd:fsck!mount",
    "virtual:cmd:grep!chimerautils",
    "virtual:cmd:install!chimerautils",
    "virtual:cmd:mkdir!chimerautils",
    "virtual:cmd:modprobe!kmod",
    "virtual:cmd:mount!mount",
    "virtual:cmd:sd-tmpfiles!sd-tools",
    "virtual:cmd:sed!chimerautils",
    "virtual:cmd:snooze!snooze",
    "virtual:cmd:sulogin!shadow",
    "virtual:cmd:systemd-tmpfiles!sd-tools",
    "virtual:cmd:udevadm!udev",
]
replaces = ["systemd-utils<255", "base-kernel<0.2"]
triggers = [
    "/usr/lib/binfmt.d",
    "/usr/lib/modprobe.d",
    "/usr/lib/modules-load.d",
    "/var/lib/swclock",
]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/tags/v{pkgver}.tar.gz"
sha256 = "b157be01907daa8413b408f30b7a53022e69a9cf9eed17204c52c91c0f7e9572"
hardening = ["vis", "cfi"]
# no tests
options = ["!check", "brokenlinks"]


def post_install(self):
    self.install_license("COPYING.md")
    self.install_file(self.files_path / "locale.conf", "etc")
    self.install_tmpfiles(self.files_path / "dinit.conf", name="dinit")
    self.install_file(
        self.files_path / "sd-tmpfiles-clean", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "tmpfiles-clean", enable=True)
    # swclock
    self.install_dir("var/lib/swclock")
    (self.destdir / "var/lib/swclock/timestamp").touch(0o644)
    # init symlink
    self.install_dir("usr/bin")
    self.install_link("usr/bin/init", "dinit")
    # x11 support
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "01dinit-env", "etc/X11/Xsession.d", mode=0o755
    )
    # sysctl additional distro files
    self.install_tmpfiles(self.files_path / "sysctl.conf", name="sysctl")
    self.install_file(
        self.files_path / "sysctl.d/sysctl.conf",
        "usr/lib/sysctl.d",
        name="10-chimera.conf",
    )
    self.install_file(
        self.files_path / "sysctl.d/sysctl-user.conf",
        "usr/lib/sysctl.d",
        name="10-chimera-user.conf",
    )
    self.install_file(
        self.files_path / "sysctl.d/bpf.conf",
        "usr/lib/sysctl.d",
        name="20-bpf.conf",
    )


@subpackage("dinit-chimera-x11")
def _x11(self):
    self.subdesc = "X11 support"
    self.depends = [self.parent]
    self.install_if = [self.parent, "xinit"]
    return [
        "etc/X11/Xsession.d",
    ]
