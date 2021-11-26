pkgname = "linux-headers-cross"
_mver = "5"
pkgver = f"{_mver}.15.5"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = ["gmake", "perl"]
depends = []
pkgdesc = "Linux API headers (cross-compiling)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org"
source = f"$(KERNEL_SITE)/kernel/v{_mver}.x/linux-{pkgver}.tar.xz"
sha256 = "e9565a301525ac81c142ceb832f9053dd5685e107dbcf753d0de4c58bc98851f"
# nothing to test
options = ["!cross", "!check"]

_targets = list(filter(
    lambda p: p[0] != self.profile().arch,
    [
        ("aarch64", "arm64"),
        ("ppc64le", "powerpc"),
        ("ppc64", "powerpc"),
        ("x86_64", "x86_64"),
        ("riscv64", "riscv"),
    ]
))

def do_build(self):
    from cbuild.util import make
    import glob

    for an, arch in _targets:
        # already done
        if (self.cwd / ("inc_" + an)).exists():
            continue

        mk = make.Make(self, jobs = 1)
        mk.invoke("mrproper", [
            "ARCH=" + arch, "CC=clang", "HOSTCC=clang", "headers"
        ])

        # remove extra files and drm headers
        for fn in self.find(".", ".*", files = True):
            self.rm(fn)

        # save the makefile
        self.cp("usr/include/Makefile", "Makefile.usr_include")
        # clean up
        self.rm("usr/include/Makefile")
        self.rm("usr/include/drm", recursive = True)
        self.mv("usr/include", "inc_" + an)
        # restore things as they were for next pass
        self.mkdir("usr/include")
        self.mv("Makefile.usr_include", "usr/include/Makefile")

def do_install(self):
    for an, arch in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            self.install_dir(f"usr/{at}/usr")
            self.install_files("inc_" + an, "usr")
            self.mv(
                self.destdir / "usr" / ("inc_" + an),
                self.destdir / f"usr/{at}/usr/include"
            )

def _gen_crossp(an, at):
    @subpackage(f"linux-headers-cross-{an}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        return [f"usr/{at}"]
    depends.append(f"linux-headers-cross-{an}={pkgver}-r{pkgrel}")

for an, arch in _targets:
    with self.profile(an) as pf:
        _gen_crossp(an, pf.triplet)
