pkgname = "stockfish"
pkgver = "19"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_build_target = "build"
make_build_args = ["optimize=no", "SUPPORTED_ARCH=true", "arch=any"]
pkgdesc = "Free UCI chess engine derived from Glaurung"
license = "GPL-3.0-or-later"
url = "https://stockfishchess.org"
_net_file = "nn-1a298aa575a0.nnue"
source = [
    f"https://github.com/official-stockfish/Stockfish/archive/sf_{pkgver}.tar.gz",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file}",
]
sha256 = [
    "519b653d0d1ffb96531d982ccbe5c6a19425e8388e0e3c2f70f34b424ab32d76",
    "1a298aa575a085434d29027978dc36867fe9c5bcea9376654b7a8eba1e52dfc2",
]
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# no check target
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / _net_file, self.build_wrksrc)


def install(self):
    self.install_bin("stockfish")
