pkgname = "nushell"
pkgver = "0.114.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=plugin,trash-support,lsp,local-socket,system-clipboard,sqlite,native-tls,network",
    "--workspace",
]
make_check_args = [
    "--",
    "--test-threads=1",
    "--skip=shell::environment::env::path_is_a_list_in_repl",
    "--skip=shell::environment::env::env_shlvl_in_exec_repl",
    "--skip=shell::environment::env::env_shlvl_in_repl",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Shell with a focus on structured data"
license = "MIT"
url = "https://www.nushell.sh"
source = f"https://github.com/nushell/nushell/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "48ef2fb6bb3ec2b1dcff87a792aeebdfab10b29f3119a62291075b17e4ad25d5"
_plugins = [
    "polars",
    "formats",
    "gstat",
    "query",
    "inc",
]

if self.profile().wordsize == 32:
    # TODO: probably fixable
    broken = "needs atomicu64"
elif self.profile().arch in ["loongarch64"]:
    broken = "unresolved import self::consts when building nix"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/nu")
    nu_autoload_path = "usr/share/nushell/vendor/autoload"
    self.install_dir(nu_autoload_path)
    for _plugin in _plugins:
        self.install_bin(
            f"target/{self.profile().triplet}/release/nu_plugin_{_plugin}"
        )
        with open(
            self.destdir / nu_autoload_path / f"enable_plugin_{_plugin}.nu", "w"
        ) as ofile:
            ofile.write(f"plugin add /usr/bin/nu_plugin_{_plugin}\n")


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")


def _genmod(pname):
    @subpackage(f"nushell-plugin-{pname}")
    def _(self):
        self.subdesc = f"{pname} plugin"
        # The scripts enabling the nushell plugins automatically are no completions
        # and make no sense in a `-nucomp` package
        self.options = ["!autosplit"]
        return [
            f"usr/bin/nu_plugin_{pname}",
            f"usr/share/nushell/vendor/autoload/enable_plugin_{pname}.nu",
        ]


for _plugin in _plugins:
    _genmod(_plugin)
