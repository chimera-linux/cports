pkgname = "musl-cross"
pkgver = "1.2.5_git20240622"
pkgrel = 1
_commit = "ab31e9d6a0fa7c5c408856c89df2dfb12c344039"
_scudo_ver = "18.1.8"
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gmake"]
makedepends = ["clang-rt-crt-cross"]
depends = ["clang-rt-crt-cross"]
pkgdesc = "Musl C library for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.musl-libc.org"
source = [
    f"https://git.musl-libc.org/cgit/musl/snapshot/musl-{_commit}.tar.gz",
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{_scudo_ver}/compiler-rt-{_scudo_ver}.src.tar.xz",
]
sha256 = [
    "18c73238e9678e7480de830701925baac0fa6cd0160bf6807b30e949196e538b",
    "e054e99a9c9240720616e927cb52363abbc8b4f1ef0286bad3df79ec8fdf892f",
]
# mirrors musl
hardening = ["!scp"]
# crosstoolchain
options = ["!cross", "!check", "!lto", "brokenlinks", "empty"]

_targetlist = [
    "aarch64",
    "armhf",
    "armv7",
    "ppc64le",
    "ppc64",
    "ppc",
    "x86_64",
    "riscv64",
]
_targets = sorted(filter(lambda p: p != self.profile().arch, _targetlist))


def post_extract(self):
    # move musl where it should be
    for f in (self.cwd / f"musl-{_commit}").iterdir():
        self.mv(f, ".")
    # prepare scudo subdir
    self.mkdir("src/malloc/scudo/scudo", parents=True)
    # move compiler-rt stuff in there
    scpath = self.cwd / f"compiler-rt-{_scudo_ver}.src/lib/scudo/standalone"
    for f in scpath.glob("*.cpp"):
        self.cp(f, "src/malloc/scudo")
    for f in scpath.glob("*.h"):
        self.cp(f, "src/malloc/scudo")
    for f in scpath.glob("*.inc"):
        self.cp(f, "src/malloc/scudo")
    self.cp(scpath / "include/scudo/interface.h", "src/malloc/scudo/scudo")
    # remove wrappers
    for f in (self.cwd / "src/malloc/scudo").glob("wrappers_*"):
        f.unlink()
    # copy in our own wrappers
    self.cp(self.files_path / "wrappers.cpp", "src/malloc/scudo")
    # now we're ready to get patched
    # but also remove musl's x86_64 asm memcpy as it's actually
    # noticeably slower than the c implementation
    self.rm("src/string/x86_64/memcpy.s")


def do_configure(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            # musl build dir
            self.mkdir(f"build-{an}", parents=True)
            # configure musl
            eargs = []
            if pf.wordsize == 32:
                # scudo needs 64-bit atomics
                eargs += ["--with-malloc=mallocng"]
            if an == "aarch64":
                # disable aarch64 memory tagging in scudo, as it fucks up qemu-user
                self.tool_flags["CXXFLAGS"] = ["-DSCUDO_DISABLE_TBI"]
            with self.stamp(f"{an}_configure") as s:
                s.check()
                self.do(
                    self.chroot_cwd / "configure",
                    *configure_args,
                    *eargs,
                    "--host=" + at,
                    wrksrc=f"build-{an}",
                    env={
                        "CC": "clang -target " + at,
                        "CXX": "clang++ -target " + at,
                    },
                )
            self.tool_flags["CXXFLAGS"] = []


def do_build(self):
    for an in _targets:
        with self.profile(an):
            self.mkdir(f"build-{an}", parents=True)
            with self.stamp(f"{an}_build") as s:
                s.check()
                self.make.build(wrksrc=self.chroot_cwd / f"build-{an}")


def do_install(self):
    self.install_license("COPYRIGHT")

    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            self.install_dir(f"usr/{at}/usr/lib")
            self.install_link(f"usr/{at}/lib", "usr/lib")
            self.make.install(
                ["DESTDIR=" + str(self.chroot_destdir / "usr" / at)],
                default_args=False,
                wrksrc=self.chroot_cwd / f"build-{an}",
            )
            self.uninstall(f"usr/{at}/lib")


def _gen_crossp(an, at):
    cond = an in _targets

    @subpackage(f"musl-cross-{an}-static", cond)
    def _ssubp(self):
        self.pkgdesc = f"{pkgdesc} (static {an} support)"
        self.depends = [f"musl-cross-{an}={pkgver}-r{pkgrel}"]
        return [f"usr/{at}/usr/lib/libc.a"]

    @subpackage(f"musl-cross-{an}", cond)
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        self.depends = [f"clang-rt-crt-cross-{an}"]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        return [f"usr/{at}"]

    if cond:
        depends.append(f"musl-cross-{an}")


for _an in _targetlist:
    with self.profile(_an) as _pf:
        _gen_crossp(_an, _pf.triplet)


@subpackage("musl-cross-static")
def _static(self):
    self.options = ["empty"]
    self.pkgdesc = f"{pkgdesc} (static)"
    self.depends = []
    for an in _targets:
        self.depends.append(f"musl-cross-{an}-static={pkgver}-r{pkgrel}")

    return []
