pkgname = "gcc-aarch64-none-elf"
_trip = pkgname.removeprefix("gcc-")
pkgver = "15.2.0"
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
    "--with-matchpd-partitions=32",
    "--with-mpc",
    "--with-mpfr",
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
license = "GPL-3.0-or-later"
url = "https://gcc.gnu.org"
source = f"$(GNU_SITE)/gcc/gcc-{pkgver}/gcc-{pkgver}.tar.xz"
sha256 = "438fd996826b0c82485a29da03a72d71d6e3541a83ec702df4271f6fe025d24e"
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
