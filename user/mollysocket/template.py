pkgname = "mollysocket"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    "--skip=config::tests::check_wildcard_endpoint",
    "--skip=utils::post_allowed::tests::test_allowed",
    "--skip=utils::post_allowed::tests::test_post",
    "--skip=ws::tls::tests::connect_untrusted_server",
    "--skip=ws::tls::tests::connect_trusted_server",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["dinit-chimera", "openssl3-devel", "rust-std", "sqlite-devel"]
pkgdesc = "Get UnifiedPush notifications on Molly"
license = "AGPL-3.0-only"
url = "https://github.com/mollyim/mollysocket"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0e6dc9c9711471156b7c52365c351f75a56b032e53209970bac733f0d9c5c3ef"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/mollysocket")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "mollysocket")
    self.install_license("LICENSE.txt")
