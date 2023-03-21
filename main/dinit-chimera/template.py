pkgname = "dinit-chimera"
_commit = "8b853603185db1c1360eb20dc0ef9c5bfcecd14d"
pkgver = "0.11"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
depends = [
    "dinit", "tzdata",
    "virtual:cmd:mkdir!chimerautils",
    "virtual:cmd:grep!chimerautils",
    "virtual:cmd:sed!chimerautils",
    "virtual:cmd:install!chimerautils",
    "virtual:cmd:awk!awk",
    "virtual:cmd:kmod!kmod",
    "virtual:cmd:modprobe!kmod",
    "virtual:cmd:fsck!mount",
    "virtual:cmd:findmnt!mount",
    "virtual:cmd:mount!mount",
    "virtual:cmd:mountpoint!mount",
    "virtual:cmd:swapon!mount",
    "virtual:cmd:sysctl!procps",
    "virtual:cmd:udevadm!udev",
]
triggers = ["/usr/lib/binfmt.d"]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/{_commit}.tar.gz"
sha256 = "819fab1341c096a100b3e86b360b29a159806f9997b79373d6380df858bc833c"
hardening = ["vis", "cfi"]
# no tests
options = ["!check", "brokenlinks"]

def post_install(self):
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_dir("usr/bin")
    self.install_link("dinit", "usr/bin/init")
    # x11 support
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "01dinit-env", "etc/X11/Xsession.d", mode = 0o755
    )

@subpackage("dinit-chimera-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "xinit"]
    return [
        "etc/X11/Xsession.d",
    ]
