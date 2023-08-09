pkgname = "ucode-intel"
pkgver = "20230808"
pkgrel = 0
archs = ["x86_64"]
makedepends = ["iucode-tool"]
depends = ["iucode-tool"]
pkgdesc = "Intel CPU microcode"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:proprietary"
url = "https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files"
source = f"{url}/archive/microcode-{pkgver}.tar.gz"
sha256 = "fe49bb719441f20335ed6004090ab38cdc374134d36d4f5d30be7ed93b820313"
options = ["!strip", "foreignelf"]


def do_build(self):
    self.do(
        "iucode_tool",
        "--write-earlyfw",
        "intel-ucode.img",
        "intel-ucode/",
    )


def do_install(self):
    self.install_files("intel-ucode", "usr/lib/firmware")
    self.install_file("intel-ucode.img", "boot")
    self.install_license("license")
    # initramfs
    self.install_file(
        self.files_path / "ucode_intel",
        "usr/share/initramfs-tools/hooks",
        mode=0o755,
    )
    self.install_file(self.files_path / "ucode-intel", "etc/default")


@subpackage("ucode-intel-full")
def _full(self):
    self.pkgdesc = f"{pkgdesc} (full cpio image)"

    return ["boot"]
