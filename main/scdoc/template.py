pkgname = "scdoc"
pkgver = "1.11.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
pkgdesc = "Tool for generating roff manual pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://git.sr.ht/~sircmpwn/scdoc"
source = f"https://git.sr.ht/~sircmpwn/scdoc/archive/{pkgver}.tar.gz"
sha256 = "1098a1ed2e087596fc0b3f657c1c8a5e00412267aa4baf3619e36824306645b1"
tool_flags = {"CFLAGS": [f"-DVERSION=\"{pkgver}\""]}

if self.cross_build:
    hostmakedepends = ["scdoc"]

def pre_build(self):
    if not self.cross_build:
        return
    self.ln_s("/usr/bin/scdoc", self.cwd / "scdoc")

def post_install(self):
    self.install_license("COPYING")
