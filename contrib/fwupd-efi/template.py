pkgname = "fwupd-efi"
pkgver = "1.6"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "meson"
configure_args = [
    # path to /usr/lib/gnuefi, fails detection with -print-multi-os-directory
    "-Defi-libdir=/usr/lib",
]
hostmakedepends = [
    "meson",
    "efivar",
    "pkgconf",
    "python-pefile",
    f"binutils-{self.profile().arch}",
]
makedepends = [
    "efivar-devel",
    "gnu-efi",
]
pkgdesc = "EFI application used by fwupd uefi-capsule"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/fwupd/fwupd-efi"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "59f90974efb29e17445e62d537c9402992fbf9f83f130317defed659222ca909"
tools = {"OBJCOPY": "gobjcopy"}
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
        f"-Defi_sbat_distro_version={pkgver}-r{pkgrel}",
    ]


@subpackage("fwupd-efi-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
