pkgname = "scdoc"
pkgver = "1.11.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
pkgdesc = "Tool for generating roff manual pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://git.sr.ht/~sircmpwn/scdoc"
source = f"https://git.sr.ht/~sircmpwn/scdoc/archive/{pkgver}.tar.gz"
sha256 = "e9ff9981b5854301789a6778ee64ef1f6d1e5f4829a9dd3e58a9a63eacc2e6f0"
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
