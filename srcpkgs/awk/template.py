pkgname = "awk"
version = "20210215"
revision = 1
bootstrap = True
_commit="c0f4e97e4561ff42544e92512bbaf3d7d1f6a671"
wrksrc = f"awk-{_commit}"
make_cmd = "bmake"
hostmakedepends = ["byacc"]
short_desc = "One true awk"
maintainer = "q66 <daniel@octaforge.org>"
license = "SMLNJ"
homepage = "https://github.com/onetrueawk/awk"
distfiles = [f"https://github.com/onetrueawk/awk/archive/{_commit}.tar.gz"]
checksum = ["8e727fc750fa96898786dc3b5b3206734cc399e4fa9f2d182ab2ad2473f31118"]

def init_configure(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.build([
        "CC=" + self.tools["CC"],
        "HOSTCC=" + self.tools["CC"],
        "CFLAGS=" + " ".join(self.CFLAGS + self.LDFLAGS + ["-DHAS_ISBLANK"]),
        "YACC=yacc -H awkgram.tab.h -o awkgram.tab.c",
    ])

def do_install(self):
    import shutil
    shutil.copy(self.abs_wrksrc / "a.out", self.abs_wrksrc / "awk")
    self.install_bin("awk")
    self.install_man("awk.1")
    self.install_license("LICENSE")
