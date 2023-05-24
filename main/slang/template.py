pkgname = "slang"
pkgver = "2.3.3"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "S-Lang programming library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.jedsoft.org/slang"
source = (
    f"https://www.jedsoft.org/releases/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
)
sha256 = "f9145054ae131973c61208ea82486d5dd10e3c5cdad23b7c4a0617743c8f5a18"
# racey; FIXME: rand module fails (likely integer overflow) but we delete that
options = ["!parallel", "!check"]


def init_configure(self):
    # force it to use CFLAGS too during linking
    self.configure_env = {
        "LDFLAGS": self.get_cflags(shell=True)
        + " "
        + self.get_ldflags(shell=True)
    }


def post_install(self):
    # clear up unnecessary junk, maybe ship in contrib?
    self.rm(self.destdir / "etc", recursive=True)
    self.rm(self.destdir / "usr/bin", recursive=True)
    self.rm(self.destdir / "usr/lib/slang", recursive=True)
    # documents largely just slsh
    self.rm(self.destdir / "usr/share/doc", recursive=True)
    self.rm(self.destdir / "usr/share/man/man1/slsh.1")
    self.rm(self.destdir / "usr/share/slsh", recursive=True)


@subpackage("slang-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
