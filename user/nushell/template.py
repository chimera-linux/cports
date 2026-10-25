pkgname = "nushell"
pkgver = "0.116.1"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
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
    # fail with 'Couldn't fit table into 0 columns!' due to lack of pty
    # https://github.com/nushell/nushell/issues/15328#issuecomment-5757878994
    "--skip=eval::eval_rendered_matches::case_3_literal_range",
    "--skip=eval::eval_rendered_matches::case_4_literal_list",
    "--skip=eval::eval_rendered_matches::case_5_literal_record",
    "--skip=eval::eval_rendered_matches::case_6_literal_table",
    "--skip=eval::eval_rendered_matches::case_8_call_spread",
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
sha256 = "0cca0c5bc9d9eb608dee00c75b6b511917df6e66c784b034468bab2ff0fbb9b4"
_plugins = [
    "polars",
    "formats",
    "gstat",
    "query",
    "inc",
]

if self.profile.wordsize == 32:
    # TODO: probably fixable
    broken = "needs atomicu64"
elif self.profile.arch in ["loongarch64"]:
    broken = "unresolved import self::consts when building nix"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "nu"))
    nu_autoload_path = "usr/share/nushell/vendor/autoload"
    self.install_dir(nu_autoload_path)
    for _plugin in _plugins:
        self.install_bin(cargo.target_path(self, f"nu_plugin_{_plugin}"))
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
