pkgname = "mollysocket"
pkgver = "1.7.1"
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
sha256 = "b380faf8ca526e92bcbc121d8ac35b88945a6f62b4602dea0df6f7c1f6bfaac7"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/mollysocket")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "mollysocket")
    self.install_license("LICENSE.txt")
