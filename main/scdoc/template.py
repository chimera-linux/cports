pkgname = "scdoc"
pkgver = "1.11.3"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
pkgdesc = "Tool for generating roff manual pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://git.sr.ht/~sircmpwn/scdoc"
source = f"https://git.sr.ht/~sircmpwn/scdoc/archive/{pkgver}.tar.gz"
sha256 = "4c5c6136540384e5455b250f768e7ca11b03fdba1a8efc2341ee0f1111e57612"
tool_flags = {"CFLAGS": [f'-DVERSION="{pkgver}"']}
hardening = ["vis", "cfi"]

if self.profile().cross:
    hostmakedepends = ["scdoc"]


def pre_build(self):
    if not self.profile().cross:
        return
    self.ln_s("/usr/bin/scdoc", self.cwd / "scdoc")


def post_install(self):
    self.install_license("COPYING")
