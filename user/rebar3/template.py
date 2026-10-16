pkgname = "rebar3"
pkgver = "3.27.3"
pkgrel = 0
hostmakedepends = ["erlang"]
depends = ["erlang"]
pkgdesc = "Erlang build tool"
license = "Apache-2.0"
url = "https://github.com/erlang/rebar3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2cf3a0d9a37ad9715fdb870b161ff61282048588ddb424362dacc22444c2d1f8"
# tests require network access
options = ["!check"]


def build(self):
    self.do("./bootstrap", "--offline")


def check(self):
    self.do("./rebar3", "ct")


def install(self):
    self.install_bin("rebar3")
    self.install_man("manpages/rebar3.1")
    self.install_completion(
        "apps/rebar/priv/shell-completion/bash/rebar3", "bash"
    )
    self.install_completion(
        "apps/rebar/priv/shell-completion/fish/rebar3.fish", "fish"
    )
    self.install_completion(
        "apps/rebar/priv/shell-completion/zsh/_rebar3", "zsh"
    )
