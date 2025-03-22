pkgname = "speakersafetyd"
pkgver = "1.0.2"
pkgrel = 0
archs = ["aarch64"]
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["alsa-lib-devel", "rust-std"]
pkgdesc = "Asahi Linux speaker safety daemon"
license = "MIT"
url = "https://github.com/AsahiLinux/speakersafetyd"
source = f"https://github.com/AsahiLinux/speakersafetyd/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "844ae3719c029e826f58c3799b6e358d189b0c42ade7a91f6c35b960cae35919"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/speakersafetyd")
    self.install_tmpfiles("speakersafetyd.tmpfiles")
    self.install_service(self.files_path / "speakersafetyd", enable=True)
    self.install_file("95-speakersafetyd.rules", "usr/lib/udev/rules.d")
    self.install_files("conf", "usr/share", name="speakersafetyd")
    self.install_license("LICENSE")
