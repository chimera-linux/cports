pkgname = "console-setup"
pkgver = "1.210"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "build-linux"
make_install_target = "install-linux"
hostmakedepends = ["gmake", "perl", "bdfresize", "perl-xml-parser"]
depends = ["perl", "kbd", "xkeyboard-config"]
pkgdesc = "Console font and keymap setup program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND custom:console-setup"
url = "https://salsa.debian.org/installer-team/console-setup"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6df6c5727efbeb2ba77682236d75210361d7184044aa71609b0698f178686bbb"
# no tests
options = ["bootstrap", "!check"]

def pre_build(self):
    self.make.invoke("maintainer-clean")

def do_install(self):
    self.install_dir("usr/bin")
    self.install_link("usr/bin", "bin")
    self.make.install([
        "prefix=" + str(self.chroot_destdir / "usr"),
        "etcdir=" + str(self.chroot_destdir / "etc")
    ])
    self.rm(self.destdir / "bin")

def post_install(self):
    self.install_license("debian/copyright")
    # service setup
    self.install_dir("usr/lib/dinit.d/boot.d")
    for scr in ["console", "keyboard"]:
        self.install_file(
            self.files_path / f"early-{scr}-setup", "usr/lib/dinit.d"
        )
        self.install_link(
            f"../early-{scr}-setup",
            f"usr/lib/dinit.d/boot.d/early-{scr}-setup"
        )

@subpackage("console-setup-dinit")
def _dinit(self):
    self.pkgdesc = f"{pkgdesc} (service files)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "dinit-chimera"]
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/lib/dinit.d/early-*"]
