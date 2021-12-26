pkgname = "binutils"
pkgver = "2.37"
pkgrel = 0
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
    "--disable-install-libbfd",
    "--disable-multilib",
    "--disable-werror",
    "--disable-shared",
    "--disable-gold",
    "--disable-nls",
    "--enable-default-hash-style=gnu",
    "--enable-deterministic-archives",
    "--enable-64-bit-bfd",
    "--enable-threads",
    "--enable-plugins",
    "--enable-relro",
]
make_cmd = "gmake"
make_install_args = ["tooldir=/usr"]
hostmakedepends = ["gmake", "flex", "texinfo"]
makedepends = ["zlib-devel"]
# binutils is a metapackage pointing to the current target binutils
depends = [f"binutils-{self.profile().arch}={pkgver}-r{pkgrel}"]
pkgdesc = "GNU binutils"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/make"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "820d9724f020a3e69cb337893a0b63c2db161dadcb0e06fc11dc29eb1e84a32c"
# FIXME maybe?
options = ["!check", "!lto"]

subpackages = []

# currently built targets, includes the native target
_targets = ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]

# configure for one target
def _configure_tgt(self, tgt):
    cargs = list(self.configure_args)

    htgt = self.profile()

    if self.cross_build:
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

    self.mkdir(f"build-{tgt.arch}", parents = True)

    self.do(
        self.chroot_cwd / "configure",
        *cargs, wrksrc = f"build-{tgt.arch}"
    )

# need to override this as we do not want to supply the default
# arguments gnu_configure supplies, especially in cross builds
def do_configure(self):
    for tgtn in _targets:
        tgtp = None
        with self.profile(tgtn) as tgt:
            tgtp = tgt

        with self.stamp(f"{tgtn}_configure") as s:
            s.check()
            _configure_tgt(self, tgtp)

def do_build(self):
    for tgtn in _targets:
        with self.stamp(f"{tgtn}_build") as s:
            s.check()
            self.make.build(wrksrc = f"build-{tgtn}")

def do_install(self):
    for tgtn in _targets:
        tgtp = None
        with self.profile(tgtn) as tgt:
            tgtp = tgt
        # native target is handled separately
        if not tgtp.cross:
            continue
        # stamp it for resuming
        with self.stamp(f"{tgtn}_install") as s:
            s.check()
            self.make.install(wrksrc = f"build-{tgtn}")
            # clean up stuff we don't want
            self.rm(self.destdir / "usr/lib/bfd-plugins", recursive = True)
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
            self.mv(
                self.destdir / "usr/lib/ldscripts",
                self.destdir / f"usr/lib/ldscripts-{tgtp.arch}"
            )

    self.make.install(wrksrc = f"build-{self.profile().arch}")

    for m in ["dlltool", "nlmconv", "windres", "windmc"]:
        self.rm(self.destdir / f"usr/share/man/man1/{m}.1", force = True)

    # provided as ld.bfd, hardlink so it's safe to remove
    for f in (self.destdir / "usr/bin").glob("*-ld"):
        self.rm(f)
        self.mv(
            self.destdir / f"usr/share/man/man1/{f.name}.1",
            self.destdir / f"usr/share/man/man1/{f.name}.bfd.1",
        )

    self.rm(self.destdir / "usr/bin/ld")
    self.mv(
        self.destdir / "usr/share/man/man1/ld.1",
        self.destdir / "usr/share/man/man1/ld.bfd.1"
    )

    # rename some tools to prefixed versions - conflicts with elftoolchain
    for p in [
        "as", "ar", "addr2line", "c++filt", "nm", "objcopy", "objdump",
        "ranlib", "readelf", "size", "strings", "strip"
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
        self.mv(
            self.destdir / "usr/bin" / p,
            self.destdir / "usr/bin" / f"g{p}"
        )
        self.mv(
            self.destdir / "usr/share/man/man1" / f"{p}.1",
            self.destdir / "usr/share/man/man1" / f"g{p}.1"
        )

    # gas can be symlinked to as though, as nothing else provides it
    self.install_link("gas", "usr/bin/as")
    self.install_link("gas.1", "usr/share/man/man1/as.1")

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

def _common(self):
    self.pkgdesc = f"{pkgdesc} (common files)"
    self.options = ["!autosplit"]

    return ["usr/lib/bfd-plugins"]

subpackages.append(("binutils-common", _common))

def _gen_subp(an, at):
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an})"
        self.depends = [f"binutils-common={pkgver}-r{pkgrel}"]

        if an == self.rparent.profile().arch:
            # native binutils is last and takes all
            return ["usr"]

        def takef():
            self.take(f"usr/bin/{at}-*")
            self.take(f"usr/lib/ldscripts-{an}")
            self.mv(
                self.destdir / f"usr/lib/ldscripts-{an}",
                self.destdir / "usr/lib/ldscripts"
            )

        return takef

    return _subp

for an in _targets:
    # this one must come last
    if an == self.profile().arch:
        continue

    with self.profile(an) as pf:
        at = pf.triplet

    subpackages.append((f"binutils-{an}", _gen_subp(an, at)))

subpackages.append((
    f"binutils-{self.profile().arch}",
    _gen_subp(self.profile().arch, self.profile().triplet)
))
