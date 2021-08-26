pkgname = "kernel-libc-headers-cross"
_mver = "5"
version = f"{_mver}.10.4"
revision = 0
wrksrc = f"linux-{version}"
make_cmd = "gmake"
hostmakedepends = ["gmake", "perl"]
depends = []
short_desc = "Linux API headers for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
homepage = "http://www.kernel.org"
distfiles = [f"$(KERNEL_SITE)/kernel/v{_mver}.x/linux-{version}.tar.xz"]
checksum = ["904e396c26e9992a16cd1cc989460171536bed7739bf36049f6eb020ee5d56ec"]
options = ["!cross"]

_targets = list(filter(
    lambda p: p[0] != current.build_profile.arch,
    [
        ("aarch64", "arm64"),
        ("ppc64le", "powerpc"),
        ("ppc64", "powerpc"),
        ("x86_64", "x86"),
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
        with self.profile(an):
            at = self.build_profile.short_triplet
            self.install_dir(f"usr/{at}/usr")
            self.install_files("inc_" + an, "usr")
            self.mv(
                self.destdir / "usr" / ("inc_" + an),
                self.destdir / f"usr/{at}/usr/include"
            )

def _gen_crossp(an, at):
    @subpackage(f"kernel-libc-headers-cross-{an}")
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        return [f"usr/{at}"]
    depends.append(f"kernel-libc-headers-cross-{an}={version}-r{revision}")

for an, arch in _targets:
    with current.profile(an):
        _gen_crossp(an, current.build_profile.short_triplet)
