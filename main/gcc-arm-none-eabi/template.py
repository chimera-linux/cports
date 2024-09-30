_trip = "arm-none-eabi"
pkgname = f"gcc-{_trip}"
pkgver = "14.2.0"
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
    "--disable-shared",
    "--disable-threads",
    "--disable-gcov",
    "--disable-tls",
    "--disable-werror",
    "--disable-tm-clone-registry",
    "--enable-__cxa_atexit",
    "--enable-c99",
    "--enable-gnu-indirect-function",
    "--enable-interwork",
    "--enable-languages=c,c++",
    "--enable-long-long",
    "--enable-multilib",
    "--enable-plugins",
    "--with-gmp",
    "--with-gnu-as",
    "--with-gnu-ld",
    "--with-libelf",
    "--with-matchpd-partitions=32",
    "--with-mpc",
    "--with-mpfr",
    "--with-multilib-list=rmprofile",
    "--with-native-system-header-dir=/include",
    "--with-newlib",
    "--with-system-zlib",
    f"--with-python-dir=share/gcc-{_trip}",
    f"--with-headers=/usr/{_trip}/include",
]
configure_gen = []
hostmakedepends = [
    f"binutils-{_trip}",
    "bison",
    "flex",
    "perl",
    "texinfo",
]
makedepends = ["zlib-ng-compat-devel", "gmp-devel", "mpfr-devel", "mpc-devel"]
depends = [f"binutils-{_trip}"]
pkgdesc = "GNU C compiler for ARM bare metal targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gcc.gnu.org"
source = f"$(GNU_SITE)/gcc/gcc-{pkgver}/gcc-{pkgver}.tar.xz"
sha256 = "a7b39bc69cbf9e25826c5a60ab26477001f7c08d85cec04bc0e29cabed6f3cc9"
patch_style = "patch"
env = {
    "CFLAGS_FOR_TARGET": "-g -Os -ffunction-sections -fdata-sections",
    "CXXFLAGS_FOR_TARGET": "-g -Os -ffunction-sections -fdata-sections",
}
nostrip_files = ["libgcc.a"]
hardening = ["!pie", "!format"]
# no tests to run
options = ["!check", "!lto", "!cross", "!scanshlibs"]


def post_install(self):
    self.uninstall("usr/share/info")
    self.uninstall("usr/share/man/man7")
    self.uninstall("usr/lib/libcc1.*", glob=True)
    # hardlinks
    self.uninstall(f"usr/bin/{_trip}-gcc")
    self.uninstall(f"usr/bin/{_trip}-c++")
    self.install_link(f"usr/bin/{_trip}-gcc", f"{_trip}-gcc-{pkgver}")
    self.install_link(f"usr/bin/{_trip}-c++", f"{_trip}-g++")
