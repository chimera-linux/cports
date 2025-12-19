# keep in sync with firmware-linux
pkgname = "ucode-amd"
pkgver = "20251125"
pkgrel = 0
archs = ["x86_64"]
makedepends = ["firmware-linux-amd-ucode"]
pkgdesc = "AMD CPU microcode"
license = "custom:linux-firmware"
url = "https://www.kernel.org"
options = ["!strip", "foreignelf", "!distlicense"]


def build(self):
    self.rm("kernel", recursive=True, force=True)
    self.mkdir("kernel/x86/microcode", parents=True)
    for f in sorted(
        (self.bldroot_path / "usr/lib/firmware/amd-ucode").glob(
            "microcode_amd*.bin"
        )
    ):
        with open(
            self.cwd / "kernel/x86/microcode/AuthenticAMD.bin", "ab"
        ) as outf:
            outf.write(f.read_bytes())
    self.touch_epoch("kernel/x86/microcode/AuthenticAMD.bin")
    with open(self.cwd / "amd-ucode.img", "wb") as outf:
        self.do(
            "cpio",
            "-o",
            "-H",
            "newc",
            "-R",
            "0:0",
            input=b"kernel/x86/microcode/AuthenticAMD.bin",
            stdout=outf,
        )


def install(self):
    self.install_file("amd-ucode.img", "boot")
    self.install_file("amd-ucode.img", "usr/lib/firmware")
    self.install_initramfs(self.files_path / "ucode_amd", name="ucode_amd")
    self.install_file(self.files_path / "ucode-amd", "etc/default")


@subpackage("ucode-amd-full")
def _(self):
    self.subdesc = "full cpio image"

    return ["boot"]
