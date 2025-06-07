pkgname = "m1n1"
pkgver = "1.4.21"
pkgrel = 0
archs = ["aarch64"]
hostmakedepends = ["gcc-aarch64-none-elf"]
pkgdesc = "Bootloader and experimentation playground for Apple Silicon"
license = "MIT"
url = "https://github.com/AsahiLinux/m1n1"
source = (
    f"https://github.com/AsahiLinux/m1n1/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "5e0239ff497a8694eaf650d292254aba7d45611f37393053558ee36886db4111"
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]


def build(self):
    self.do(
        "env",
        "-u",
        "CFLAGS",
        "-u",
        "LDFLAGS",
        "-u",
        "CPPFLAGS",
        "-u",
        "CXXFLAGS",
        "--",
        "make",
        f"-j{self.make_jobs}",
        "ARCH=aarch64-none-elf-",
        "CC=aarch64-none-elf-gcc",
        "RELEASE=1",
    )


def install(self):
    self.install_file("build/m1n1.bin", "usr/lib/asahi-boot")
    self.install_file("m1n1.conf.example", "usr/share/m1n1")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_license("LICENSE")
