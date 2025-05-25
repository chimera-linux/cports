pkgname = "xh"
pkgver = "0.24.1"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    # need net
    "--skip=cert_without_key",
    "--skip=compress_request_body_online",
    "--skip=digest_auth_with_response_meta",
    "--skip=formatted_certificate_expired_message",
    "--skip=good_tls_version",
    "--skip=http1_0",
    "--skip=http1_1",
    "--skip=http2",
    "--skip=successful_digest_auth",
    "--skip=unsuccessful_digest_auth",
    "--skip=use_ipv4",
    "--skip=verify_default_yes",
    "--skip=verify_explicit_yes",
    "--skip=verify_no",
    "--skip=verify_valid_file",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "oniguruma-devel",
    "rust-std",
]
pkgdesc = "Tool for sending HTTP requests"
license = "MIT"
url = "https://github.com/ducaale/xh"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c5902052c66e20fd2c0b49db14edb027f54500b502108327e17260c64a42edee"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/xh")
    self.install_license("LICENSE")
    self.install_man("doc/xh.1")
    self.install_completion("completions/_xh", "zsh")
    self.install_completion("completions/xh.bash", "bash")
    self.install_completion("completions/xh.fish", "fish")
    self.install_completion("completions/xh.nu", "nushell")
