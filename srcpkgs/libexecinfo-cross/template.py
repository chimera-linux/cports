pkgname = "libexecinfo-cross"
version = "1.1"
revision = 0
wrksrc = f"libexecinfo-{version}"
build_style = "gnu_makefile"
makedepends = ["musl-cross"]
depends = ["musl-cross"]
short_desc = "BSD licensed clone of the GNU backtrace (cross compiling)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "http://www.freshports.org/devel/libexecinfo"
distfiles = [f"http://distcache.freebsd.org/local-distfiles/itetcu/libexecinfo-{version}.tar.bz2"]
checksum = ["c9a21913e7fdac8ef6b33250b167aa1fc0a7b8a175145e26913a4c19d8a59b1f"]
nocross = True

_targets = ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]

from cbuild import cpu

def do_build(self):
    import shutil

    for an in _targets:
        if cpu.target() == an:
            continue
        # skip already done pass
        if (self.abs_wrksrc / f"libexecinfo.a.{an}").exists():
            continue

        with self.profile(an):
            at = self.build_profile.short_triplet
            self.make.build([
                f"CC=clang -target {at} --sysroot /usr/{at}",
                "PREFIX=/usr",
                "CFLAGS=" + self.get_cflags(shell = True),
                "LDFLAGS=--unwindlib=none " + self.get_ldflags(shell = True),
                "AR=" + self.get_tool("AR")
            ])
            shutil.move(
                self.abs_wrksrc / "libexecinfo.a",
                self.abs_wrksrc / f"libexecinfo.a.{an}"
            )
            shutil.move(
                self.abs_wrksrc / "libexecinfo.so.1",
                self.abs_wrksrc / f"libexecinfo.so.{an}"
            )

def do_install(self):
    import shutil

    for an in _targets:
        if cpu.target() == an:
            continue
        with self.profile(an):
            at = self.build_profile.short_triplet
            self.install_dir(f"usr/{at}/usr/lib/pkgconfig")
            self.install_dir(f"usr/{at}/usr/include")
            self.install_dir(f"usr/{at}/usr/lib")
            shutil.move(
                self.abs_wrksrc / f"libexecinfo.a.{an}",
                self.abs_wrksrc / "libexecinfo.a"
            )
            shutil.move(
                self.abs_wrksrc / f"libexecinfo.so.{an}",
                self.abs_wrksrc / "libexecinfo.so.1"
            )
            self.install_file(
                self.abs_wrksrc / "libexecinfo.pc",
                f"usr/{at}/usr/lib/pkgconfig"
            )
            self.install_file(
                self.abs_wrksrc / "execinfo.h",
                f"usr/{at}/usr/include"
            )
            self.install_file(
                self.abs_wrksrc / "libexecinfo.a",
                f"usr/{at}/usr/lib"
            )
            self.install_file(
                self.abs_wrksrc / "libexecinfo.so.1",
                f"usr/{at}/usr/lib",
                mode = 0o755
            )
            self.install_link(
                "libexecinfo.so.1", f"usr/{at}/usr/lib/libexecinfo.so"
            )

def _gen_crossp(an, at):
    @subpackage(f"libexecinfo-cross-{an}", cpu.target() != an)
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        self.depends = [f"musl-cross-{an}"]
        self.options = ["!scanshlibs"]
        return [f"usr/{at}"]
    if cpu.target() != an:
        depends.append(f"libexecinfo-cross-{an}={version}-r{revision}")

for an in _targets:
    with current.profile(an):
        _gen_crossp(an, current.build_profile.short_triplet)
