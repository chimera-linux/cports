pkgname = "binutils"
version = "2.35.1"
revision = 4
bootstrap = True
make_install_args = ["tooldir=/usr"]
hostmakedepends = []
makedepends = ["zlib-devel"]
short_desc = "GNU binary utilities"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/binutils/"

from cbuild import sites, cpu

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.xz"]
checksum = ["3ced91db9bf01182b7e420eab68039f2083aed0a214c0424e257eae3ddee8607"]

patch_args = "-Np1"

subpackages = []

if not current.bootstrapping:
    hostmakedepends += ["flex", "perl", "texinfo"]
    checkdepends = ["bc"]

def get_triplet(self):
    if not self.triplet:
        import importlib
        bp = importlib.import_module("cbuild.build_profiles." + cpu.target())
        return bp.XBPS_TRIPLET
    else:
        return self.triplet

def do_configure(self):
    conf = []

    if self.bootstrapping:
        conf.append("--disable-install-libbfd")

    if self.cross_build:
        conf.append("--host=" + self.cross_triplet)
        conf.append("--with-build-sysroot=" + self.cross_base)

    if cpu.match_target("ppc*"):
        conf.append("--enable-secureplt")
    elif cpu.match_target("x86_64*"):
        conf.append("--enable-targets=x86_64-pep")
    elif cpu.match_target("i686*"):
        conf.append("--enable-targets=x86_64-linux-gnu,x86_64-pep")

    self.do(self.chroot_wrksrc / "configure", [
        "--build=" + get_triplet(self),
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--mandir=/usr/share/man",
        "--infodir=/usr/share/info",
        "--without-debuginfod",
        "--disable-werror",
        "--disable-shared",
        "--disable-nls",
        "--disable-gold",
        "--disable-multilib",
        "--enable-threads",
        "--enable-plugins",
        "--enable-relro",
        "--enable-deterministic-archives",
        "--enable-64-bit-bfd",
        "--enable-ld=default",
        "--enable-default-hash-style=gnu",
        "--with-system-zlib",
        "--with-mmap",
        "--with-pic",
    ] + conf, build = True)

def init_build(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.build()

def do_install(self):
    triplet = get_triplet(self)

    self.make.install()

    # remove ld (hardlink)
    self.unlink("usr/bin/ld")
    self.install_link("ld.bfd", "usr/bin/ld")

    # remove useless manpages
    for f in ["dlltool", "nlmconv", "windres", "windmc"]:
        self.unlink("usr/share/man/man1/" + f + ".1", missing_ok = True)

    # create triplet symlinks
    for f in (self.destdir / "usr/bin").iterdir():
        self.install_link(f.name, f"usr/bin/{triplet}-{f.name}")

    import shutil
    shutil.rmtree(self.destdir / "usr/share/info", ignore_errors = True)

def _devel(self):
    self.depends = ["zlib-devel"]
    self.short_desc = short_desc + " - development files"

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")

    return install

if not current.bootstrapping:
    subpackages.append(("binutils-devel", _devel))
