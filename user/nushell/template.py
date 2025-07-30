pkgname = "nushell"
pkgver = "0.106.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=plugin,trash-support,sqlite,native-tls",
    "--workspace",
]
make_check_args = [
    "--",
    "--skip=shell::environment::env::path_is_a_list_in_repl",
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
sha256 = "3e24044c354d050a850b69dc77c99cc503542c3d9d75fed0aef1c12fefdf380b"
_plugins = [
    "polars",
    "formats",
    "gstat",
    "query",
    "inc",
]


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
