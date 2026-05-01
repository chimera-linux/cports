pkgname = "fwupd-efi"
pkgver = "1.8"
pkgrel = 0
archs = ["aarch64", "armv7", "loongarch64", "riscv64", "x86_64"]
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = [
    f"binutils-{self.profile().arch}",
    "efivar",
    "meson",
    "pkgconf",
    "python-pefile",
]
makedepends = [
    "efivar-devel",
    "gnu-efi",
]
pkgdesc = "EFI application used by fwupd uefi-capsule"
license = "LGPL-2.1-or-later"
url = "https://github.com/fwupd/fwupd-efi"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c9f1f9b9b967ea50eb0b478f0d7693d6673d4cd76c8e7eb80c55fc44ec928925"
tools = {"LD": "ld.bfd", "OBJCOPY": "gobjcopy"}
tool_flags = {"LDFLAGS": ["-fuse-ld=bfd"]}
options = ["!cross"]

_sbat = False

# FIXME: on aarch64 enabling sbat results in crt0 relocation failures
if self.profile().arch == "x86_64":
    _sbat = True

if _sbat:
    configure_args += [
        "-Defi_sbat_distro_id=chimera",
        "-Defi_sbat_distro_summary=Chimera Linux",
        "-Defi_sbat_distro_pkgname=fwupd-efi",
        "-Defi_sbat_distro_url=https://chimera-linux.org",
        f"-Defi_sbat_distro_version={self.full_pkgver}",
    ]


@subpackage("fwupd-efi-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
