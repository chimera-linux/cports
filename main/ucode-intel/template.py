pkgname = "ucode-intel"
pkgver = "20240813"
pkgrel = 1
archs = ["x86_64"]
hostmakedepends = ["iucode-tool"]
depends = ["iucode-tool"]
pkgdesc = "Intel CPU microcode"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:proprietary"
url = "https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files"
source = f"{url}/archive/microcode-{pkgver}.tar.gz>intelmoment.tar.gz"
sha256 = "f46cfe1d8be8d3c2c5a0fb63fc4d48c7dd1444f34346f0e42ad92c706cb90e79"
options = ["!strip", "foreignelf"]


def build(self):
    self.do(
        "iucode_tool",
        "--write-earlyfw",
        "intel-ucode.img",
        "intel-ucode/",
    )


def install(self):
    self.install_files("intel-ucode", "usr/lib/firmware")
    self.install_file("intel-ucode.img", "boot")
    self.install_license("license")
    self.install_initramfs(self.files_path / "ucode_intel", name="ucode_intel")
    self.install_file(self.files_path / "ucode-intel", "etc/default")


@subpackage("ucode-intel-full")
def _(self):
    self.subdesc = "full cpio image"

    return ["boot"]
