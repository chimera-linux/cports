pkgname = "efibootmgr"
pkgver = "18"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["efivar-devel", "popt-devel", "linux-headers"]
pkgdesc = "Tool to modify the UEFI Boot Manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/rhboot/efibootmgr"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "2b195f912aa353f0d11f21f207684c91460fbc37f9a4f2673e63e5e32d108b10"

# TODO: kernel hook?

match self.profile().arch:
    case "x86_64":
        _loader = "grubx64.efi"
    case "aarch64":
        _loader = "grubaa64.efi"
    case "riscv64":
        _loader = "grubriscv64.efi"
    case _:
        broken = f"Unsupported architecture: {self.profile().arch}"

def init_configure(self):
    if self.profile().cross:
        self.make_build_args += [f"CROSS_COMPILE={self.profile().triplet}-"]

def do_build(self):
    from cbuild.util import make
    make.Make(self).build([
        "EXTRA_CFLAGS=" + self.get_cflags(shell = True),
        "EFIDIR=chimera", "EFI_LOADER=" + _loader
    ])

def do_install(self):
    self.install_bin("src/efibootdump")
    self.install_man("src/efibootdump.8")
    self.install_bin("src/efibootmgr")
    self.install_man("src/efibootmgr.8")

# FIXME visibility
hardening = ["!vis"]
