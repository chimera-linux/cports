pkgname = "mksh"
pkgver = "59c"
pkgrel = 0
checkdepends = ["chimerautils", "perl"]
pkgdesc = "MirBSD Korn Shell"
maintainer = "Christiano Haesbaert <haesbaert@haesbaert.org>"
license = "MirOS"
url = "http://www.mirbsd.org/mksh.htm"
source = f"https://mbsd.evolvis.org/MirOS/dist/mir/mksh/mksh-R59c.tgz"
sha256 = "77ae1665a337f1c48c61d6b961db3e52119b38e58884d1c89684af31f87bc506"
hardening = ["vis", "cfi"]

def build(self):
    self.do("sh", "Build.sh")

def check(self):
    self.do("./test.sh", "-C", "regress:no-ctty")

def install(self):
    self.install_bin("mksh")
    self.install_man("mksh.1")
    self.install_man("lksh.1")
    self.install_file("dot.mkshrc", "usr/share/examples/mksh")

def post_install(self):
    self.install_shell("/usr/bin/mksh")
