pkgname = "binutils"
pkgver = "2.45"
_llvmver = "21.1.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--libdir=/usr/lib",
    "--mandir=/usr/share/man",
    "--infodir=/usr/share/info",
    "--without-debuginfod",
    "--with-system-zlib",
    "--with-mmap",
    "--with-pic",
    "--with-zstd",
    "--disable-install-libbfd",
    "--disable-multilib",
    "--disable-werror",
    "--disable-shared",
    "--disable-gprofng",
    "--disable-gold",
    "--disable-nls",
    "--enable-default-hash-style=gnu",
    "--enable-deterministic-archives",
    "--enable-new-dtags",
    "--enable-64-bit-bfd",
    "--enable-threads",
    "--enable-plugins",
    "--enable-relro",
]
make_install_args = ["tooldir=/usr"]
hostmakedepends = [
    "bison",
    "flex",
    "pkgconf",
    "texinfo",
]
makedepends = [
    "jansson-devel",
    "linux-headers",
    "llvm-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
# binutils is a metapackage pointing to the current target binutils
depends = [self.with_pkgver(f"binutils-{self.profile().arch}")]
pkgdesc = "GNU binutils"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/binutils"
source = [
    f"$(GNU_SITE)/binutils/binutils-{pkgver}.tar.xz",
    f"!https://raw.githubusercontent.com/llvm/llvm-project/llvmorg-{_llvmver}/llvm/tools/gold/gold-plugin.cpp>gold-plugin-{_llvmver}.cpp",
]
sha256 = [
    "c50c0e7f9cb188980e2cc97e4537626b1672441815587f1eab69d2a1bfbef5d2",
    "c165183819e41b25e708ea8d0938ae43125b946509016ee8550db3c09da9237b",
]
# resistance is futile
options = ["!check", "!lto", "linkundefver", "empty"]

# currently built targets, includes the native target
_targets = [
    "aarch64",
    "armv7",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "ppc",
    "riscv64",
    "x86_64",
]


def post_extract(self):
    self.cp(
        self.sources_path / f"gold-plugin-{_llvmver}.cpp", "gold-plugin.cpp"
    )


# configure for one target
def _configure_tgt(self, tgt):
    cargs = [*self.configure_args]

    htgt = self.profile()

    if self.profile().cross:
        cargs += [
            f"--host={htgt.triplet}",
            f"--with-build-sysroot={htgt.sysroot}",
        ]

    if tgt.cross:
        cargs += [
            f"--target={tgt.triplet}",
        ]

    match tgt.arch:
        case "ppc64le" | "ppc64" | "ppc":
            cargs += ["--enable-secureplt"]
        case "x86_64":
            cargs += ["--enable-targets=x86_64-pep"]
        case "i686":
            cargs += ["--enable-targets=x86_64-linux-gnu,x86_64-pep"]

    self.mkdir(f"build-{tgt.arch}", parents=True)

    self.do(self.chroot_cwd / "configure", *cargs, wrksrc=f"build-{tgt.arch}")


# need to override this as we do not want to supply the default
# arguments gnu_configure supplies, especially in cross builds
def configure(self):
    for tgtn in _targets:
        tgtp = None
        with self.profile(tgtn) as tgt:
            tgtp = tgt

        with self.stamp(f"{tgtn}_configure") as s:
            s.check()
            _configure_tgt(self, tgtp)


def build(self):
    from cbuild.util import compiler

    for tgtn in _targets:
        with self.stamp(f"{tgtn}_build") as s:
            s.check()
            self.make.build(wrksrc=f"build-{tgtn}")

    compiler.CXX(self).invoke(
        ["gold-plugin.cpp"],
        "LLVMgold.so",
        flags=[
            "-Iinclude",
            "-shared",
            "-fvisibility=hidden",
            "-fPIC",
            "-lLLVM",
            "-Wl,--no-undefined",
        ],
    )


def install(self):
    for tgtn in _targets:
        tgtp = None
        with self.profile(tgtn) as tgt:
            tgtp = tgt
        # native target is handled separately
        if not tgtp.cross:
            continue
        self.make.install(wrksrc=f"build-{tgtn}")
        # clean up stuff we don't want
        self.uninstall("usr/lib/bfd-plugins")
        # remove non-prefix binaries
        for f in (self.destdir / "usr/bin").glob("*"):
            if f.name.find("-") > 0:
                continue
            f.unlink()
        # remove non-prefix manpages
        for f in (self.destdir / "usr/share/man/man1").glob("*"):
            if f.name.find("-") > 0:
                continue
            f.unlink()
        # temporary
        self.rename(
            "usr/lib/ldscripts",
            f"ldscripts-{tgtp.arch}",
        )

    self.make.install(wrksrc=f"build-{self.profile().arch}")

    # lto plugin
    self.install_file("LLVMgold.so", "usr/lib", mode=0o755)
    self.install_link("usr/lib/bfd-plugins/LLVMgold.so", "../LLVMgold.so")

    for m in ["dlltool", "windres", "windmc"]:
        self.uninstall(f"usr/share/man/man1/{m}.1")

    # provided as ld.bfd, hardlink so it's safe to remove
    for f in (self.destdir / "usr/bin").glob("*-ld"):
        self.rm(f)
        self.rename(
            f"usr/share/man/man1/{f.name}.1",
            f"{f.name}.bfd.1",
        )

    self.uninstall("usr/bin/ld")
    self.rename(
        "usr/share/man/man1/ld.1",
        "ld.bfd.1",
    )

    # rename some tools to prefixed versions - conflicts with llvm
    for p in [
        "as",
        "ar",
        "addr2line",
        "c++filt",
        "nm",
        "objcopy",
        "objdump",
        "ranlib",
        "readelf",
        "size",
        "strings",
        "strip",
    ]:
        # rename cross versions
        for f in (self.destdir / "usr/bin").glob(f"*-{p}"):
            tf = f.with_name(f.name.removesuffix(p) + f"g{p}")
            self.mv(f, tf)
            if p == "as":
                f.symlink_to(tf.name)
        for f in (self.destdir / "usr/share/man/man1").glob(f"*-{p}.1"):
            tf = f.with_name(f.name.removesuffix(f"{p}.1") + f"g{p}.1")
            self.mv(f, tf)
            if p == "as":
                f.symlink_to(tf.name)
        # rename native version
        self.rename(f"usr/bin/{p}", f"g{p}")
        self.rename(f"usr/share/man/man1/{p}.1", f"g{p}.1")

    # gas can be symlinked to as though, as nothing else provides it
    self.install_link("usr/bin/as", "gas")
    self.install_link("usr/share/man/man1/as.1", "gas.1")

    tgt = self.profile()

    # create triplet symlinks for native
    for p in (self.destdir / "usr/bin").glob("*"):
        if p.name.find("-") > 0:
            continue
        p.with_name(f"{tgt.triplet}-{p.name}").symlink_to(p.name)

    for p in (self.destdir / "usr/share/man/man1").glob("*.1"):
        if p.name.find("-") > 0:
            continue
        p.with_name(f"{tgt.triplet}-{p.name}").symlink_to(p.name)


@subpackage("binutils-common")
def _(self):
    self.subdesc = "common files"
    self.options = ["!splitstatic"]

    return [
        "usr/lib/bfd-plugins",
        "usr/lib/LLVMgold.so",
    ]


def _gen_subp(an, native):
    @subpackage(f"binutils-{an}")
    def _(self):
        self.subdesc = an
        self.depends = [self.with_pkgver("binutils-common")]

        if native:
            # native binutils is last and takes all
            return ["usr"]

        with self.rparent.profile(an) as pf:
            at = pf.triplet

        def takef():
            self.take(f"cmd:{at}-*")
            self.take(f"usr/lib/ldscripts-{an}")
            self.mv(
                self.destdir / f"usr/lib/ldscripts-{an}",
                self.destdir / "usr/lib/ldscripts",
            )

        return takef


for _an in _targets:
    # this one must come last
    if _an == self.profile().arch:
        continue
    _gen_subp(_an, False)

_gen_subp(self.profile().arch, True)
