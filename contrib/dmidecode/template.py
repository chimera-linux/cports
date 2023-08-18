pkgname = "dmidecode"
pkgver = "3.5"
pkgrel = 0
# smbios/dmi support
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_install_args = ["prefix=/usr", "sbindir=/usr/bin"]
pkgdesc = "Utility for reporting system hardware"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://nongnu.org/dmidecode"
source = f"https://download.savannah.gnu.org/releases/dmidecode/dmidecode-{pkgver}.tar.xz"
sha256 = "79d76735ee8e25196e2a722964cf9683f5a09581503537884b256b01389cc073"
hardening = ["vis", "cfi"]
# none present
options = ["!check"]
