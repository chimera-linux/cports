pkgname = "gnu-efi"
pkgver = "3.0.15"
pkgrel = 0
archs = ["x86_64", "aarch64", "riscv64"]
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = ["gmake"]
pkgdesc = "Development libraries for EFI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "(BSD-2-Clause AND BSD-3-Clause) OR GPL-2.0-or-later"
url = "https://sourceforge.net/projects/gnu-efi"
source = f"$(SOURCEFORGE_SITE)/gnu-efi/gnu-efi-{pkgver}.tar.bz2"
sha256 = "931a257b9c5c1ba65ff519f18373c438a26825f2db7866b163e96d1b168f20ea"
hardening = ["!int"]
# no relevant test suite
options = ["!check", "!debug", "!strip", "!lto", "!splitstatic"]


def init_configure(self):
    eargs = ["PREFIX=/usr", "INSTALLROOT=" + str(self.chroot_destdir)]
    with self.profile("host"):
        eargs += ["HOSTCC=" + self.get_tool("CC")]
    with self.profile("target"):
        eargs += ["CC=" + self.get_tool("CC")]

    self.make_build_args += eargs
    self.make_install_args += eargs
