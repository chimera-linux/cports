pkgname = "go-task"
pkgver = "3.42.1"
pkgrel = 1
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/go-task/task/v3/internal/version.version=v{pkgver}"
    " -X github.com/go-task/task/v3/internal/version.sum=chimera",
    "./cmd/task",
]
hostmakedepends = ["go"]
pkgdesc = "Task runner / simpler Make alternative written in Go"
license = "MIT"
url = "https://taskfile.dev"
source = f"https://github.com/go-task/task/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ebda29f1ec14e3e78f6d1e89136822c8177cc0b6d214fac8b1f027abce3c9042"
# conditionally disabled check
options = []

# test suite expects amd64
if self.profile().arch != "x86_64":
    options += ["!check"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_completion("completion/fish/task.fish", "fish", "task")
    self.install_completion("completion/bash/task.bash", "bash", "task")
    self.install_completion("completion/zsh/_task", "zsh", "task")
