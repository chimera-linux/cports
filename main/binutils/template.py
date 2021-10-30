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
pkgdesc = "GNU Make build tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/make"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "820d9724f020a3e69cb337893a0b63c2db161dadcb0e06fc11dc29eb1e84a32c"
# FIXME maybe?
options = ["!check"]

# need to override this as we do not want to supply the default
# arguments gnu_configure supplies, especially in cross builds
def do_configure(self):
    cargs = list(self.configure_args)
    tgt = self.profile()

    if self.cross_build:
        cargs += [
            f"--host={tgt.short_triplet}",
            "--with-build-sysroot={tgt.sysroot}",
        ]

    match tgt.arch:
        case "ppc64le" | "ppc64" | "ppc":
            cargs += ["--enable-secureplt"]
        case "x86_64":
            cargs += ["--enable-targets=x86_64-pep"]
        case "i686":
            cargs += ["--enable-targets=x86_64-linux-gnu,x86_64-pep"]

    self.mkdir("build", parents = True)

    self.do(
        self.chroot_cwd / "configure",
        cargs, wrksrc = "build"
    )

def post_install(self):
    for m in ["dlltool", "nlmconv", "windres", "windmc"]:
        self.rm(self.destdir / f"usr/share/man/man1/{m}.1", force = True)

    # provided as ld.bfd, hardlink so it's safe to remove
    self.rm(self.destdir / "usr/bin/ld")

    # rename some tools to prefixed versions - conflicts with elftoolchain
    for p in [
        "as", "ar", "addr2line", "c++filt", "nm", "objcopy", "objdump",
        "ranlib", "readelf", "size", "strings", "strip"
    ]:
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

    tgt = self.profile()

    # create triplet symlinks
    for p in (self.destdir / "usr/bin").glob("*"):
        p.with_name(f"{tgt.short_triplet}-{p.name}").symlink_to(p.name)
