pkgname = "tealdeer"
pkgver = "1.6.1"
pkgrel = 0
build_style = "cargo"
make_check_args = [
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
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl-devel"]
pkgdesc = "Alternative implementation of tldr"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/dbrgn/tealdeer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d42db25a56a72faec173c86192656c5381281dc197171f385fccffd518930430"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_completion("completion/bash_tealdeer", "bash", name="tldr")
    self.install_completion("completion/zsh_tealdeer", "zsh", name="tldr")
    self.install_completion("completion/fish_tealdeer", "fish", name="tldr")
