pkgname = "speakersafetyd"
pkgver = "1.1.2"
pkgrel = 0
archs = ["aarch64"]
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "libcap-progs", "pkgconf"]
makedepends = ["alsa-lib-devel", "rust-std"]
pkgdesc = "Asahi Linux speaker safety daemon"
license = "MIT"
url = "https://github.com/AsahiLinux/speakersafetyd"
source = f"https://github.com/AsahiLinux/speakersafetyd/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b3ccbbf4c3ee0da537203186f80eb8f3cc16037bf41f4cd0de50b7cd25dd713f"
file_modes = {
    "usr/bin/speakersafetyd": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/speakersafetyd": {
        "security.capability": "cap_sys_nice+ep",
    },
}
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/speakersafetyd")
    self.install_tmpfiles("speakersafetyd.tmpfiles")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "speakersafetyd", enable=True)
    self.install_file("95-speakersafetyd.rules", "usr/lib/udev/rules.d")
    self.install_files("conf", "usr/share", name="speakersafetyd")
    self.install_license("LICENSE")
