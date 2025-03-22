pkgname = "tealdeer"
pkgver = "1.7.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features", "--features", "native-tls"]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=test_autoupdate_cache",
    "--skip=test_create_cache_directory_path",
    "--skip=test_pager_flag_enable",
    "--skip=test_quiet_cache",
    "--skip=test_quiet_failures",
    "--skip=test_quiet_old_cache",
    "--skip=test_spaces_find_command",
    "--skip=test_update_cache",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel"]
pkgdesc = "Alternative implementation of tldr"
license = "MIT"
url = "https://github.com/tealdeer-rs/tealdeer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d0675b9aa48c00e78abafc318b9bfbcb7ea3cce63e58a42c1f9e2395abcfe0e8"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/tldr")
    self.install_license("LICENSE-MIT")
    self.install_completion("completion/bash_tealdeer", "bash", "tldr")
    self.install_completion("completion/zsh_tealdeer", "zsh", "tldr")
    self.install_completion("completion/fish_tealdeer", "fish", "tldr")
