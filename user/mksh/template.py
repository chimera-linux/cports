pkgname = "mksh"
pkgver = "59c"
pkgrel = 0
checkdepends = ["perl"]
pkgdesc = "MirBSD Korn shell"
license = "MirOS"
url = "http://www.mirbsd.org/mksh.htm"
source = f"https://mbsd.evolvis.org/MirOS/dist/mir/mksh/mksh-R{pkgver}.tgz"
sha256 = "77ae1665a337f1c48c61d6b961db3e52119b38e58884d1c89684af31f87bc506"
tool_flags = {"CFLAGS": ['-DMKSHRC_PATH="/usr/share/mksh/mkshrc"']}
hardening = ["vis", "cfi"]


def build(self):
    self.do("sh", "Build.sh")


def check(self):
    self.do("./test.sh", "-C", "regress:no-ctty")


def install(self):
    self.install_bin("mksh")
    self.install_man("mksh.1")
    self.install_file(self.files_path / "mkshrc", "usr/share/mksh")
    self.install_file("dot.mkshrc", "usr/share/mksh")
    self.install_shell("/usr/bin/mksh")
