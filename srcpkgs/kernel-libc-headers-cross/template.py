pkgname = "kernel-libc-headers-cross"
_mver = "5"
version = f"{_mver}.10.4"
revision = 0
wrksrc = f"linux-{version}"
make_cmd = "gmake"
depends = []
short_desc = "Linux API headers for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
homepage = "http://www.kernel.org"

from cbuild import sites, cpu

distfiles = [f"{sites.kernel}/kernel/v{_mver}.x/linux-{version}.tar.xz"]
checksum = ["904e396c26e9992a16cd1cc989460171536bed7739bf36049f6eb020ee5d56ec"]

hostmakedepends = ["gmake", "perl"]

_targets = [("aarch64", "arm64"), ("ppc64le", "powerpc"), ("x86_64", "x86")]

def do_build(self):
    from cbuild.util import make
    import glob, shutil

    for an, arch in _targets:
        if cpu.target() == an:
            continue

        # already done
        if (self.abs_wrksrc / ("inc_" + an)).exists():
            continue

        mk = make.Make(self, jobs = 1)
        mk.invoke("mrproper", [
            "ARCH=" + arch, "CC=clang", "HOSTCC=clang", "headers"
        ])

        # remove extra files and drm headers
        for fn in self.find(".*", files = True, root = self.abs_wrksrc):
            self.unlink(fn, root = self.abs_wrksrc)

        # save the makefile
        shutil.copy(
            self.abs_wrksrc / "usr/include/Makefile",
            self.abs_wrksrc / "Makefile.usr_include"
        )
        # clean up
        self.unlink("usr/include/Makefile", root = self.abs_wrksrc)
        self.rmtree("usr/include/drm", root = self.abs_wrksrc)
        shutil.move(
            self.abs_wrksrc / "usr/include", self.abs_wrksrc / ("inc_" + an)
        )
        # restore things as they were for next pass
        (self.abs_wrksrc / "usr/include").mkdir()
        shutil.move(
            self.abs_wrksrc / "Makefile.usr_include",
            self.abs_wrksrc / "usr/include/Makefile"
        )

def do_install(self):
    import shutil

    for an, arch in _targets:
        if cpu.target() == an:
            continue
        with self.profile(an):
            self.install_dir(f"usr/{self.build_profile.triplet}/usr")
            self.install_files("inc_" + an, "usr")
            shutil.move(
                self.destdir / "usr" / ("inc_" + an),
                self.destdir / f"usr/{self.build_profile.triplet}/usr/include"
            )

def _gen_crossp(an, at):
    @subpackage(f"kernel-libc-headers-cross-{an}", cpu.target() != an)
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        return [f"usr/{at}"]
    if cpu.target() != an:
        depends.append(f"kernel-libc-headers-cross-{an}={version}-r{revision}")

for an, arch in _targets:
    with current.profile(an):
        _gen_crossp(an, current.build_profile.triplet)
