pkgname = "efibootmgr"
pkgver = "17"
pkgrel = 0
_commit = "b9fedd6b6f57055164bc361bc5cf16a602843c6e"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["efivar-devel", "popt-devel", "linux-headers"]
pkgdesc = "Tool to modify the UEFI Boot Manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/rhboot/efibootmgr"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "06061ebf96d28522f5a20b592305e71b91d3fb479ddcce41dadb5180da16d8d8"

# TODO: kernel hook?

match self.profile().arch:
    case "x86_64":
        _loader = "grubx64.efi"
    case "aarch64":
        _loader = "grubaa64.efi"
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
