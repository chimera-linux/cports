pkgname = "gnu-efi"
pkgver = "3.0.17"
pkgrel = 0
# riscv64 does not build but also nothing needs it there
archs = ["x86_64", "aarch64"]
build_style = "makefile"
make_use_env = True
hostmakedepends = ["pkgconf", f"binutils-{self.profile().arch}"]
pkgdesc = "Development libraries for EFI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/gnu-efi"
source = f"$(SOURCEFORGE_SITE)/gnu-efi/gnu-efi-{pkgver}.tar.bz2"
sha256 = "7807e903349343a7a142ebb934703a2872235e89688cf586c032b0a1087bcaf4"
tools = {
    "LD": "ld.bfd",
    "OBJCOPY": "gobjcopy",
}
tool_flags = {
    "CFLAGS": ["-fno-integrated-as", "-Wno-incompatible-pointer-types"]
}
hardening = ["!int"]
# no relevant test suite
options = ["!check", "!debug", "!strip", "!lto", "!relr", "!splitstatic"]


def init_configure(self):
    eargs = ["PREFIX=/usr", "INSTALLROOT=" + str(self.chroot_destdir)]
    with self.profile("host"):
        eargs += ["HOSTCC=" + self.get_tool("CC")]
    with self.profile("target"):
        eargs += [
            "CC=" + self.get_tool("CC"),
            "LD=" + self.get_tool("LD"),
            "OBJCOPY=" + self.get_tool("OBJCOPY"),
        ]

    self.make_build_args += eargs
    self.make_install_args += eargs
