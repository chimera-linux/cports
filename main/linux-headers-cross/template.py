pkgname = "linux-headers-cross"
pkgver = "6.9.8"
pkgrel = 0
hostmakedepends = ["gmake", "perl"]
depends = []
pkgdesc = "Linux API headers for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.kernel.org"
source = f"$(KERNEL_SITE)/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "f048267b7b88316c9ca708c68d15a9ae802dcfc943c3188c1273eb958c433281"
# nothing to test
options = ["!cross", "!check", "empty"]

_targetlist = [
    ("aarch64", "arm64"),
    ("armhf", "arm"),
    ("armv7", "arm"),
    ("ppc64le", "powerpc"),
    ("ppc64", "powerpc"),
    ("ppc", "powerpc"),
    ("x86_64", "x86_64"),
    ("riscv64", "riscv"),
]
_targets = list(filter(lambda p: p[0] != self.profile().arch, _targetlist))


def do_build(self):
    for an, arch in _targets:
        # already done
        if (self.cwd / ("inc_" + an)).exists():
            continue

        self.do(
            "gmake",
            "ARCH=" + arch,
            "CC=clang",
            "HOSTCC=clang",
            "mrproper",
            "headers",
        )

        # remove extra files and drm headers
        for fn in self.find(".", ".*", files=True):
            self.rm(fn)

        # save the makefile
        self.cp("usr/include/Makefile", "Makefile.usr_include")
        # clean up
        self.rm("usr/include/Makefile")
        self.rm("usr/include/drm", recursive=True)
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
                self.destdir / f"usr/{at}/usr/include",
            )


def _crosshdr(an, arch):
    _cond = (an, arch) in _targets

    @subpackage(f"linux-headers-cross-{an}", _cond)
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        with self.rparent.profile(an) as pf:
            return [f"usr/{pf.triplet}"]

    if _cond:
        depends.append(f"linux-headers-cross-{an}={pkgver}-r{pkgrel}")


for _an, _arch in _targetlist:
    _crosshdr(_an, _arch)
