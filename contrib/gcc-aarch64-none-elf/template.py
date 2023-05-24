_trip = "aarch64-none-elf"
pkgname = f"gcc-{_trip}"
pkgver = "12.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--target={_trip}",
    f"--with-sysroot=/usr/{_trip}",
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--libdir=/usr/lib",
    "--mandir=/usr/share/man",
    "--infodir=/usr/share/info",
    "--disable-nls",
    "--disable-decimal-float",
    "--disable-libffi",
    "--disable-libgomp",
    "--disable-libmudflap",
    "--disable-libquadmath",
    "--disable-libssp",
    "--disable-libstdcxx-pch",
    "--disable-libstdc__-v3",
    "--disable-multilib",
    "--disable-shared",
    "--disable-threads",
    "--disable-gcov",
    "--disable-tls",
    "--disable-werror",
    "--disable-tm-clone-registry",
    "--enable-__cxa_atexit",
    "--enable-c99",
    "--enable-gnu-indirect-function",
    "--enable-languages=c,c++",
    "--enable-long-long",
    "--enable-plugins",
    "--with-gmp",
    "--with-gnu-as",
    "--with-gnu-ld",
    "--with-libelf",
    "--with-mpc",
    "--with-mpfr",
    "--with-native-system-header-dir=/include",
    "--with-newlib",
    "--with-system-zlib",
    f"--with-python-dir=share/gcc-{_trip}",
    f"--with-headers=/usr/{_trip}/include",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    f"binutils-{_trip}",
    "bison",
    "flex",
    "perl",
    "texinfo",
]
makedepends = ["zlib-devel", "gmp-devel", "mpfr-devel", "mpc-devel"]
depends = [f"binutils-{_trip}"]
pkgdesc = "GNU C compiler for ARM bare metal targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gcc.gnu.org"
source = f"$(GNU_SITE)/gcc/gcc-{pkgver}/gcc-{pkgver}.tar.xz"
sha256 = "e549cf9cf3594a00e27b6589d4322d70e0720cdd213f39beb4181e06926230ff"
env = {
    "CFLAGS_FOR_TARGET": "-g -Os -ffunction-sections -fdata-sections",
    "CXXFLAGS_FOR_TARGET": "-g -Os -ffunction-sections -fdata-sections",
}
nostrip_files = ["libgcc.a"]
hardening = ["!pie"]
# no tests to run
options = ["!check", "!lto", "!cross", "!scanshlibs"]
exec_wrappers = [
    ("/usr/bin/llvm-objdump", "objdump"),
    ("/usr/bin/llvm-readelf", "readelf"),
]


def post_install(self):
    self.rm(self.destdir / "usr/share/info", recursive=True)
    self.rm(self.destdir / "usr/share/man/man7", recursive=True)
    for f in (self.destdir / "usr/lib").glob("libcc1.*"):
        f.unlink()
    # hardlinks
    self.rm(self.destdir / f"usr/bin/{_trip}-gcc")
    self.rm(self.destdir / f"usr/bin/{_trip}-c++")
    self.install_link(f"{_trip}-gcc-{pkgver}", f"usr/bin/{_trip}-gcc")
    self.install_link(f"{_trip}-g++", f"usr/bin/{_trip}-c++")


configure_gen = []
