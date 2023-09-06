pkgname = "dinit-chimera"
pkgver = "0.99.1"
pkgrel = 2
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
depends = [
    "dinit",
    "tzdata",
    "virtual:cmd:mkdir!chimerautils",
    "virtual:cmd:grep!chimerautils",
    "virtual:cmd:sed!chimerautils",
    "virtual:cmd:install!chimerautils",
    "virtual:cmd:awk!chimerautils",
    "virtual:cmd:kmod!kmod",
    "virtual:cmd:modprobe!kmod",
    "virtual:cmd:fsck!mount",
    "virtual:cmd:findmnt!mount",
    "virtual:cmd:mount!mount",
    "virtual:cmd:mountpoint!mount",
    "virtual:cmd:swapon!mount",
    "virtual:cmd:sysctl!procps",
    "virtual:cmd:sulogin!shadow",
    "virtual:cmd:udevadm!udev",
    "virtual:cmd:systemd-tmpfiles!systemd-tmpfiles",
]
triggers = ["/usr/lib/binfmt.d"]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/tags/v{pkgver}.tar.gz"
sha256 = "78a972c5db3610a2f4ed06b9d7e3f7556ef6a1013b2e956a7448608ed60f3417"
hardening = ["vis", "cfi"]
# no tests
options = ["!check", "brokenlinks"]


def post_install(self):
    self.install_license("COPYING.md")
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_dir("usr/bin")
    self.install_link("dinit", "usr/bin/init")
    # x11 support
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "01dinit-env", "etc/X11/Xsession.d", mode=0o755
    )


@subpackage("dinit-chimera-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "xinit"]
    return [
        "etc/X11/Xsession.d",
    ]
