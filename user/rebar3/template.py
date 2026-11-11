pkgname = "rebar3"
pkgver = "3.28.0"
pkgrel = 0
hostmakedepends = ["erlang"]
depends = ["erlang"]
pkgdesc = "Erlang build tool"
license = "Apache-2.0"
url = "https://github.com/erlang/rebar3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4a8bdd1fc845742833988db73012b232a3e9fd048011189ae9e0cecf70bdb7a2"
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
