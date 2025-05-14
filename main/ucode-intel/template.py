pkgname = "ucode-intel"
pkgver = "20250512"
pkgrel = 0
archs = ["x86_64"]
hostmakedepends = ["iucode-tool"]
depends = ["iucode-tool"]
pkgdesc = "Intel CPU microcode"
license = "custom:proprietary"
url = "https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files"
source = f"{url}/archive/microcode-{pkgver}.tar.gz"
sha256 = "041af7d2f5791a47c1e914abd7d6255de4d4fc61b0f8e49ada6ee7014bcc3614"
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
