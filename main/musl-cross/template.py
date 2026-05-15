pkgname = "musl-cross"
pkgver = "1.2.6"
pkgrel = 2
_commit = "9fa28ece75d8a2191de7c5bb53bed224c5947417"
_mimalloc_ver = "2.2.7"
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
configure_gen = []
makedepends = ["clang-rt-crt-cross"]
depends = ["clang-rt-crt-cross"]
pkgdesc = "Musl C library for cross-compiling"
license = "MIT"
url = "http://www.musl-libc.org"
source = [
    f"https://git.musl-libc.org/cgit/musl/snapshot/musl-{_commit}.tar.gz",
    f"https://github.com/microsoft/mimalloc/archive/refs/tags/v{_mimalloc_ver}.tar.gz",
]
source_paths = [".", "mimalloc"]
sha256 = [
    "d3baf222d234f2121e71b7eabd0c17667b7a3733b3077e99f9920c69cb5899df",
    "8e0ed89907a681276bff2e49e9a048b47ba51254ab60daf6b3c220acac456a95",
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
    "loongarch64",
]
_targets = sorted(filter(lambda p: p != self.profile().arch, _targetlist))


def post_extract(self):
    # reported in libc.so --version
    with open(self.cwd / "VERSION", "w") as f:
        f.write(pkgver)
    # copy in our mimalloc unified source
    self.cp(self.files_path / "mimalloc-verify-syms.sh", ".")
    self.cp(self.files_path / "mimalloc.c", "mimalloc/src")
    # now we're ready to get patched
    # but also remove musl's x86_64 asm memcpy as it's actually
    # noticeably slower than the c implementation
    self.rm("src/string/x86_64/memcpy.s")
    self.rm("src/string/x86_64/memmove.s")


def configure(self):
    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            # musl build dir
            self.mkdir(f"build-{an}", parents=True)
            self.mkdir(f"src/malloc/external-{pf.arch}", parents=True)
            # configure musl
            eargs = []
            if pf.wordsize == 32:
                eargs += ["--with-malloc=mallocng"]
            else:
                eargs += [f"--with-malloc=external-{pf.arch}"]
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


def build(self):
    for an in _targets:
        with self.profile(an) as pf:
            eargs = []
            if pf.wordsize != 32:
                eargs += [
                    f"EXTRA_OBJ=$(srcdir)/src/malloc/external-{pf.arch}/mimalloc.o"
                ]
            with self.stamp(f"{an}_build") as s:
                s.check()
                self.make.build(eargs, wrksrc=self.chroot_cwd / f"build-{an}")


def install(self):
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
    def _(self):
        self.subdesc = f"static {an} support"
        self.depends = [self.with_pkgver(f"musl-cross-{an}")]
        return [f"usr/{at}/usr/lib/libc.a"]

    @subpackage(f"musl-cross-{an}", cond)
    def _(self):
        self.subdesc = f"{an} support"
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
def _(self):
    self.options = ["empty"]
    self.subdesc = "static"
    self.depends = []
    for an in _targets:
        self.depends.append(self.with_pkgver(f"musl-cross-{an}-static"))

    return []
