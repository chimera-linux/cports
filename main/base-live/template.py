pkgname = "base-live"
pkgver = "0.1"
pkgrel = 3
build_style = "meta"
depends = [
    "cryptsetup-scripts",
    "firmware-linux-soc",
    "lvm2",
    "lvm2-dm",
]
pkgdesc = "Packages to be included in official live images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"

# grub for local installations without net access
match self.profile().arch:
    case "aarch64":
        depends += ["grub-arm64-efi"]
    case "ppc" | "ppc64" | "ppc64le":
        depends += ["grub-powerpc-ieee1275"]
    case "riscv64":
        depends += ["grub-riscv64-efi"]
    case "x86_64":
        depends += ["grub-i386-efi", "grub-i386-pc", "grub-x86_64-efi"]

# extra bootloaders on efi targets, again for offline install
if self.profile().arch in ["aarch64", "riscv64", "x86_64"]:
    depends += ["limine", "systemd-boot"]
