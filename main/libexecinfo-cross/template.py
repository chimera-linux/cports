pkgname = "libexecinfo-cross"
pkgver = "1.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["musl-cross"]
depends = ["musl-cross"]
pkgdesc = "Cross-toolchain version of libexecinfo"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://www.freshports.org/devel/libexecinfo"
source = f"http://distcache.freebsd.org/local-distfiles/itetcu/libexecinfo-{pkgver}.tar.bz2"
sha256 = "c9a21913e7fdac8ef6b33250b167aa1fc0a7b8a175145e26913a4c19d8a59b1f"
# no test suite
options = ["!cross", "!check", "!lto"]

_targets = list(filter(
    lambda p: p != self.profile().arch,
    ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
))

def do_build(self):
    for an in _targets:
        # skip already done pass
        if (self.cwd / f"libexecinfo.a.{an}").exists():
            continue

        with self.profile(an) as pf:
            at = pf.triplet
            self.make.build([
                f"CC=clang -target {at} --sysroot /usr/{at}",
                "PREFIX=/usr",
                "CFLAGS=" + self.get_cflags(shell = True),
                "LDFLAGS=--unwindlib=none " + self.get_ldflags(shell = True),
                "AR=" + self.get_tool("AR")
            ])
            self.mv("libexecinfo.a", f"libexecinfo.a.{an}")
            self.mv("libexecinfo.so.1", f"libexecinfo.so.{an}")

def do_install(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            self.install_dir(f"usr/{at}/usr/lib/pkgconfig")
            self.install_dir(f"usr/{at}/usr/include")
            self.install_dir(f"usr/{at}/usr/lib")
            self.mv(f"libexecinfo.a.{an}", "libexecinfo.a")
            self.mv(f"libexecinfo.so.{an}", "libexecinfo.so.1")
            self.install_file("libexecinfo.pc", f"usr/{at}/usr/lib/pkgconfig")
            self.install_file("execinfo.h", f"usr/{at}/usr/include")
            self.install_file("libexecinfo.a", f"usr/{at}/usr/lib")
            self.install_file(
                "libexecinfo.so.1", f"usr/{at}/usr/lib", mode = 0o755
            )
            self.install_link(
                "libexecinfo.so.1", f"usr/{at}/usr/lib/libexecinfo.so"
            )

def _gen_crossp(an, at):
    @subpackage(f"libexecinfo-cross-{an}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        self.depends = [f"musl-cross-{an}"]
        self.options = [
            "foreignelf", "!scanshlibs", "!scanrundeps",
            "!scanpkgconf", "!splitstatic"
        ]
        return [f"usr/{at}"]
    depends.append(f"libexecinfo-cross-{an}={pkgver}-r{pkgrel}")

for an in _targets:
    with self.profile(an) as pf:
        _gen_crossp(an, pf.triplet)
