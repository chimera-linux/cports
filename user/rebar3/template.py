pkgname = "rebar3"
pkgver = "3.27.1"
pkgrel = 0
hostmakedepends = ["erlang"]
depends = ["erlang"]
pkgdesc = "Erlang build tool"
license = "Apache-2.0"
url = "https://github.com/erlang/rebar3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e34cf5e8f25fc7e59b2ff5c56fed507cf1378d4eef2a4aa7957b3c7e80812d64"
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
