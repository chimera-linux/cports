pkgname = "gcc-riscv64-unknown-elf"
_trip = pkgname.removeprefix("gcc-")
pkgver = "16.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--target={_trip}",
    f"--with-sysroot=/usr/{_trip}",
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
pkgdesc = "GNU C compiler for RISC-V embedded targets"
license = "GPL-3.0-or-later"
url = "https://gcc.gnu.org"
source = f"$(GNU_SITE)/gcc/gcc-{pkgver}/gcc-{pkgver}.tar.xz"
sha256 = "50efb4d94c3397aff3b0d61a5abd748b4dd31d9d3f2ab7be05b171d36a510f79"
env = {
    "CFLAGS_FOR_TARGET": "-g -Os -ffunction-sections -fdata-sections",
    "CXXFLAGS_FOR_TARGET": "-g -Os -ffunction-sections -fdata-sections",
}
nostrip_files = ["libgcc.a"]
# fails to build
hardening = ["!pie", "!int", "!format"]
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
