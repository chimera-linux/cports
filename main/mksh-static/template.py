pkgname = "mksh-static"
pkgver = "59c"
pkgrel = 0
checkdepends = ["perl", "bsded"]
pkgdesc = "MirBSD Korn Shell (static build)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MirOS"
url = "https://www.mirbsd.org/mksh.htm"
source = [
    f"http://www.mirbsd.org/MirOS/dist/mir/mksh/mksh-R{pkgver}.tgz",
    ("http://www.mirbsd.org/TaC-mksh.txt", False)
]
sha256 = [
    "77ae1665a337f1c48c61d6b961db3e52119b38e58884d1c89684af31f87bc506",
    "8a53fe4d643fb7341e6c94653d63d3d813d8d849fc1d9dfe5dc49ab2fb48aee9"
]
tool_flags = {"CFLAGS": ["-static"], "LDFLAGS": ["-static"]}
options = ["bootstrap"]

def do_build(self):
    self.do("sh", [self.chroot_cwd / "Build.sh", "-r"])

def do_check(self):
    # the shebang points to itself
    self.do(self.chroot_cwd / "test.sh", ["-C", "regress:no-ctty"])

def do_install(self):
    self.install_bin("mksh.static")

    self.install_license(self.sources_path / "TaC-mksh.txt")

    # register shell
    self.install_dir("etc/shells.d")
    self.install_link("/usr/bin/mksh.static", "etc/shells.d/mksh.static")
