pkgname = "tealdeer"
pkgver = "1.7.0"
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
makedepends = ["rust-std", "openssl-devel"]
pkgdesc = "Alternative implementation of tldr"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tealdeer-rs/tealdeer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "940fe96a44571f395ac8349e5cba7ddb9231ce526bee07a9eb68f02c32f7da7b"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/tldr")
    self.install_license("LICENSE-MIT")
    self.install_completion("completion/bash_tealdeer", "bash", "tldr")
    self.install_completion("completion/zsh_tealdeer", "zsh", "tldr")
    self.install_completion("completion/fish_tealdeer", "fish", "tldr")
