pkgname = "base-live"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = [
    "cryptsetup-scripts",
    "device-mapper",
    "firmware-linux-soc",
    "lvm2",
    "mtools",
    "xorriso",
]
pkgdesc = "Packages to be included in official live images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


match self.profile().arch:
    case "aarch64":
        depends += ["grub-arm64-efi"]
    case "ppc" | "ppc64" | "ppc64le":
        depends += ["grub-powerpc-ieee1275"]
    case "riscv64":
        depends += ["grub-riscv64-efi"]
    case "x86_64":
        depends += ["grub-i386-efi", "grub-i386-pc", "grub-x86_64-efi"]
